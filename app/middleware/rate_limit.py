from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from starlette.responses import (
    JSONResponse,
)

from app.services.rate_limit_service import (
    RateLimitService,
)

from app.core.constants import (
    DEFAULT_RATE_LIMIT,
    DEFAULT_RATE_WINDOW,
)


class RateLimitMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        ip = request.client.host

        key = f"rl:{ip}"

        allowed = (
            RateLimitService.check_limit(
                key,
                DEFAULT_RATE_LIMIT,
                DEFAULT_RATE_WINDOW,
            )
        )

        if not allowed:

            return JSONResponse(
                status_code=429,
                content={
                    "detail":
                    "Rate limit exceeded"
                },
            )

        return await call_next(
            request
        )
