from fastapi import (
    APIRouter,
    Depends,
)

from app.api.dependencies.rbac import (
    require_role,
)

from app.services.upstream_service import (
    UpstreamServiceManager,
)

from app.services.proxy_service import (
    ProxyService,
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get(
    "/test"
)
def admin_test(
    current_user=Depends(
        require_role(
            "admin"
        )
    )
):

    return {
        "message": "Admin access granted",
        "user": current_user.username,
    }


@router.get(
    "/services"
)
def services():

    return (
        UpstreamServiceManager
        .list_services()
    )


@router.get(
    "/health-check"
)
async def health_check():

    response = (
        await ProxyService.get(
            "https://httpbin.org/get"
        )
    )

    return response.json()
