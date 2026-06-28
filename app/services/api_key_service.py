from app.repositories.api_key_repository import (
    ApiKeyRepository,
)


class ApiKeyService:

    def __init__(
        self,
        repository: ApiKeyRepository,
    ):
        self.repository = repository

    def create(
        self,
        owner: str,
    ):

        return self.repository.create(
            owner
        )

    def validate(
        self,
        key: str,
    ):

        return self.repository.get_by_key(
            key
        )

    def list_keys(
        self,
    ):

        return self.repository.list_all()

    def revoke(
        self,
        api_key_id: int,
    ):

        return self.repository.delete(
            api_key_id
        )
