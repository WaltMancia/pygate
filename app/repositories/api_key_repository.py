import secrets

from sqlalchemy.orm import Session

from app.models.api_key import ApiKey


class ApiKeyRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        owner: str,
    ):

        api_key = ApiKey(
            key=secrets.token_hex(32),
            owner=owner,
            enabled=True,
        )

        self.db.add(api_key)

        self.db.commit()

        self.db.refresh(api_key)

        return api_key

    def get_by_key(
        self,
        key: str,
    ):

        return (
            self.db.query(ApiKey)
            .filter(
                ApiKey.key == key,
                ApiKey.enabled.is_(True),
            )
            .first()
        )

    def list_all(
        self,
    ):

        return (
            self.db.query(ApiKey)
            .order_by(ApiKey.id)
            .all()
        )

    def delete(
        self,
        api_key_id: int,
    ):

        api_key = (
            self.db.query(ApiKey)
            .filter(
                ApiKey.id == api_key_id
            )
            .first()
        )

        if api_key:

            self.db.delete(api_key)

            self.db.commit()

        return api_key
