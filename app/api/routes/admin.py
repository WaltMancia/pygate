from fastapi import (
    APIRouter,
    Depends,
)

from app.api.dependencies.rbac import (
    require_role,
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
