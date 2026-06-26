from fastapi import (
    Depends,
    HTTPException,
    status,
)

from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)

from app.core.jwt import (
    decode_access_token,
)

from app.core.request_context import (
    current_user,
)

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
):

    token = credentials.credentials

    payload = decode_access_token(
        token
    )

    if payload is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    current_user.set(
        payload
    )

    return payload
