from fastapi import (
    APIRouter,
    Request,
    HTTPException,
)

from fastapi.responses import (
    Response,
)

from app.services.proxy_service import (
    ProxyService,
)

from app.services.upstream_service import (
    UpstreamServiceManager,
)

from app.services.circuit_breaker import (
    CircuitBreaker,
)

from app.services.cache_service import (
    CacheService,
)

from app.services.metrics_service import (
    MetricsService,
)

router = APIRouter(
    prefix="/proxy",
    tags=["Proxy"],
)


@router.api_route(
    "/{service}/{path:path}",
    methods=[
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    ],
)
async def proxy_request(
    service: str,
    path: str,
    request: Request,
):

    MetricsService.increment_requests()

    upstream = (
        UpstreamServiceManager
        .get_service(service)
    )

    if not upstream:

        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )

    if CircuitBreaker.is_open(
        service
    ):

        raise HTTPException(
            status_code=503,
            detail="Circuit breaker open",
        )

    cache_key = (
        f"{service}:{path}"
    )

    if request.method == "GET":

        cached = (
            CacheService.get(
                cache_key
            )
        )

        if cached:

            MetricsService.increment_cache_hit()

            return Response(
                content=cached,
                media_type="application/json",
            )

        MetricsService.increment_cache_miss()

    body = await request.body()

    try:

        response = (
            await ProxyService.forward(
                method=request.method,
                url=f"{upstream}/{path}",
                headers=dict(
                    request.headers
                ),
                body=body,
            )
        )

    except Exception:

        CircuitBreaker.record_failure(
            service
        )

        raise HTTPException(
            status_code=502,
            detail="Upstream service unavailable",
        )

    MetricsService.increment_proxied()

    if response.status_code >= 500:

        CircuitBreaker.record_failure(
            service
        )

    else:

        CircuitBreaker.record_success(
            service
        )

    if (
        request.method == "GET"
        and response.status_code == 200
    ):

        CacheService.set(
            cache_key,
            response.text,
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get(
            "content-type"
        ),
    )
