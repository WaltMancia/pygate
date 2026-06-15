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
            minutes=settings.JWT_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": str(user_id),
        "username": username,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )
