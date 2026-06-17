from fastapi import (
    APIRouter,
    Depends,
)

from app.dependencies.permissions import (
    require_permission,
)

from app.api.dependencies.rate_limit import (
    rate_limit,
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/users")
async def get_users(
    allowed=Depends(
        require_permission(
            "users.read"
        )
    )
):
    return {
        "message":
        "Protected user list"
    }


@router.post("/users")
async def create_user(
    allowed=Depends(
        require_permission(
            "users.create"
        )
    )
):
    return {
        "message":
        "User created"
    }


@router.get(
    "/test"
)
def admin_test(
    current_user=Depends(
        require_role(
            "admin"
        )
    ),
    _=Depends(
        rate_limit(
            limit=5,
            window=60,
        )
    ),
):
