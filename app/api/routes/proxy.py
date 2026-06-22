from fastapi.responses import (
    Response,
)
from fastapi import (
    APIRouter,
    HTTPException,
)

from app.services.upstream_service import (
    UpstreamServiceManager,
)

from app.services.proxy_service import (
    ProxyService,
)

router = APIRouter(
    prefix="/proxy",
    tags=["Proxy"],
)


@router.get(
    "/{service}"
)
async def proxy_get(
    service: str,
):

    upstream = (
        UpstreamServiceManager
        .get_service(
            service
        )
    )from fastapi import (
        APIRouter,
        Request,
        HTTPException,
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

    upstream = (
        UpstreamServiceManager
        .get_service(service)
    )

    if not upstream:

        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )

    body = await request.body()

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

    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get(
            "content-type"
        ),
    )

    if not upstream:

        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )

    response = (
        await ProxyService.get(
            upstream
        )
    )

    return response.json()
