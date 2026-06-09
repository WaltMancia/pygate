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
        data.username == "admin"
        and
        data.password == "admin123"
    ):

        token = (
            create_access_token(
                user_id=1,
                username="admin",
            )
        )

        return {
            "access_token":
                token
        }

    return {
        "message":
        "Invalid credentials"
    }


@router.get("/me")
async def me(
    request: Request
):
    return request.state.user
