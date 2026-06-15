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
