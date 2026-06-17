from fastapi import (
    Depends,
    HTTPException,
)

from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)

from sqlalchemy.orm import Session

from app.db.session import (
    get_db,
)

from app.core.jwt import (
    decode_token,
)

from app.repositories.user_repository import (
    UserRepository,
)

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(
        get_db
    ),
):

    payload = decode_token(
        credentials.credentials
    )

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    username = payload.get(
        "username"
    )

    repo = UserRepository(db)

    user = repo.get_by_username(
        username
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user
