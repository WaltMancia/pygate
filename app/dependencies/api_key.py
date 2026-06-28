from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.repositories.api_key_repository import (
    ApiKeyRepository,
)

from app.services.api_key_service import (
    ApiKeyService,
)


def get_api_key_service(
    db: Session = Depends(get_db),
):

    repository = ApiKeyRepository(
        db
    )

    return ApiKeyService(
        repository
    )
