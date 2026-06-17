from fastapi import (
    Request,
    HTTPException,
)

from app.services.rate_limit_service import (
    RateLimitService,
)


def rate_limit(
    limit: int,
    window: int,
):

    def checker(
        request: Request,
    ):

        ip = (
            request.client.host
        )

        key = (
            f"rl:{ip}"
        )

        allowed = (
            RateLimitService.check_limit(
                key,
                limit,
                window,
            )
        )

        if not allowed:

            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded",
            )

    return checker
