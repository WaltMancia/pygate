from fastapi import (
    APIRouter,
    Depends,
)

from app.schemas.api_key import (
    ApiKeyCreate,
    ApiKeyResponse,
)

from app.services.api_key_service import (
    ApiKeyService,
)

from app.api.dependencies.api_key import (
    get_api_key_service,
)

router = APIRouter(
    prefix="/admin/api-keys",
    tags=["API Keys"],
)


@router.post(
    "",
    response_model=ApiKeyResponse,
)
def create_api_key(
    payload: ApiKeyCreate,
    service: ApiKeyService = Depends(
        get_api_key_service
    ),
):

    return service.create(
        payload.owner
    )


@router.get(
    "",
    response_model=list[ApiKeyResponse],
)
def list_api_keys(
    service: ApiKeyService = Depends(
        get_api_key_service
    ),
):

    return service.list_keys()


@router.delete(
    "/{api_key_id}",
)
def revoke_api_key(
    api_key_id: int,
    service: ApiKeyService = Depends(
        get_api_key_service
    ),
):

    service.revoke(
        api_key_id
    )

    return {
        "message": "API Key revoked"
    }
