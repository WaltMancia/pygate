from fastapi import (
    APIRouter,
    Request
)

from pydantic import (
    BaseModel,
)

from app.core.security import (
    create_access_token,
)

from app.core.permissions import (
    ADMIN_PERMISSIONS,
    VIEWER_PERMISSIONS,
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


class LoginRequest(
    BaseModel
):
    username: str
    password: str


@router.post("/login")
async def login(
    data: LoginRequest,
):

    if (
        data.username == "viewer"
        and
        data.password == "viewer123"
    ):

        token = create_access_token(
            user_id=2,
            username="viewer",
            role="viewer",
            permissions=VIEWER_PERMISSIONS,
        )

    return {
        "access_token": token
    }


@router.get("/me")
async def me(
    request: Request
):
    return request.state.user
