from datetime import (
    datetime,
    timedelta,
)

import jwt

from app.core.config import (
    settings,
)


def create_access_token(
    user_id: int,
    username: str,
):
    payload = {
        "sub": str(user_id),
        "username": username,
        "role": role,
        "permissions": permissions,
        "exp": datetime.utcnow()
        + timedelta(hours=8),
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )


def verify_token(
    token: str,
):
    return jwt.decode(
        token,
        settings.JWT_SECRET,
        algorithms=[
            settings.JWT_ALGORITHM
        ],
    )
