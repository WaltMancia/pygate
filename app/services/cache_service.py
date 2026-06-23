from app.core.redis_client import (
    redis_client,
)


class CacheService:

    @staticmethod
    def get(
        key: str,
    ):

        return redis_client.get(
            key
        )

    @staticmethod
    def set(
        key: str,
        value: str,
        ttl: int = 30,
    ):

        redis_client.setex(
            key,
            ttl,
            value,
        )
