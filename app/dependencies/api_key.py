from fastapi import (
    Header,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.db.session import (
    SessionLocal,
)

from app.models.api_key import (
    ApiKey,
)


def validate_api_key(
    x_api_key: str = Header(
        default=None
    ),
):

    if not x_api_key:

        raise HTTPException(
            status_code=401,
            detail="API Key required",
        )

    db: Session = SessionLocal()

    key = (
        db.query(ApiKey)
        .filter(
            ApiKey.api_key
            == x_api_key
        )
        .first()
    )

    db.close()

    if not key:

        raise HTTPException(
            status_code=401,
            detail="Invalid API Key",
        )

    return key
