from app.core.redis_client import (
    redis_client,
)


class RateLimitService:

    @staticmethod
    def check_limit(
        key: str,
        limit: int,
        window: int,
    ):

        current = redis_client.get(
            key
        )

        if current is None:

            redis_client.setex(
                key,
                window,
                1,
            )

            return True

        current = int(current)

        if current >= limit:

            return False

        redis_client.incr(
            key
        )

        return True
