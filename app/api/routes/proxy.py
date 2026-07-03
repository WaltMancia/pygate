import time

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    Response,
)

from app.core.upstreams import (
    UPSTREAMS,
)

from app.services.proxy_service import (
    ProxyService,
)

from app.services.gateway_analytics_service import (
    GatewayAnalyticsService,
)

from app.api.dependencies.analytics import (
    get_gateway_analytics_service,
)

router = APIRouter(
    tags=["Gateway"],
)


@router.api_route(
    "/{service}/{path:path}",
    methods=[
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "OPTIONS",
    ],
)
async def proxy(
    service: str,
    path: str,
    request: Request,
    analytics: GatewayAnalyticsService = Depends(
        get_gateway_analytics_service,
    ),
):

    upstream = UPSTREAMS.get(
        service
    )

    if upstream is None:

        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )

    target_url = (
        f"{upstream}/{path}"
    )

    body = await request.body()

    trace_id = getattr(
        request.state,
        "trace_id",
        None,
    )

    started = time.perf_counter()

    response = await ProxyService.forward(
        method=request.method,
        url=target_url,
        headers=dict(request.headers),
        body=body,
        trace_id=trace_id,
    )

    latency = (
        time.perf_counter()
        - started
    ) * 1000

    analytics.register(
        service=service,
        endpoint=request.url.path,
        method=request.method,
        status_code=response.status_code,
        latency=latency,
    )

    excluded_headers = {
        "content-length",
        "transfer-encoding",
        "connection",
        "content-encoding",
    }

    headers = {
        key: value
        for key, value in response.headers.items()
        if key.lower() not in excluded_headers
    }

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=headers,
        media_type=response.headers.get(
            "content-type"
        ),
    )
