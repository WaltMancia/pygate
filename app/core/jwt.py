from datetime import (
    datetime,
    timedelta,
    UTC,
)

import jwt

from app.core.config import (
    settings,
)


def create_access_token(
    user_id: int,
    username: str,
):

    expire = (
        datetime.now(UTC)
        + timedelta(
            minutes=settings.jwt_expire_minutes
        )
    )

    payload = {
        "sub": str(user_id),
        "username": username,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )
