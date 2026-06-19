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
