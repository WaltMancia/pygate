from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.db.session import (
    get_db,
)

from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)

from app.services.auth_service import (
    AuthService,
)

from app.api.dependencies.auth import (
    get_current_user,
)

from app.models.user import (
    User,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    payload: LoginRequest,
    db: Session = Depends(
        get_db
    ),
):

    service = AuthService(db)

    token = service.login(
        payload.username,
        payload.password,
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    return {
        "access_token": token
    }


@router.get(
    "/me"
)
def me(
    current_user: User = Depends(
        get_current_user
    ),
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "role_id": current_user.role_id,
    }
