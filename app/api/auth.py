from fastapi import (
    APIRouter,
    HTTPException,
)

from pydantic import (
    BaseModel,
)

from app.db.session import (
    SessionLocal,
)

from app.repositories.user_repository import (
    UserRepository,
)

from app.core.passwords import (
    verify_password,
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

    db = SessionLocal()

    try:

        repo = UserRepository(db)

        user = repo.get_by_username(
            data.username
        )

        if not user:

            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        if not verify_password(
            data.password,
            user.password_hash,
        ):

            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        permissions = (
            ADMIN_PERMISSIONS
            if user.role == "admin"
            else VIEWER_PERMISSIONS
        )

        token = create_access_token(
            user_id=user.id,
            username=user.username,
            role=user.role,
            permissions=permissions,
        )

        return {
            "access_token": token
        }

    finally:
        db.close()
