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
