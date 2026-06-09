from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from fastapi.responses import (
    JSONResponse,
)

from app.core.security import (
    verify_token,
)


PUBLIC_PATHS = {
    "/health",
    "/auth/login",
}


class AuthMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        if request.url.path in PUBLIC_PATHS:
            return await call_next(
                request
            )

        auth_header = (
            request.headers.get(
                "Authorization"
            )
        )

        if not auth_header:

            return JSONResponse(
                status_code=401,
                content={
                    "message":
                    "Missing token"
                },
            )

        try:

            token = (
                auth_header.replace(
                    "Bearer ",
                    ""
                )
            )

            payload = verify_token(
                token
            )

            request.state.user = (
                payload
            )

        except Exception:

            return JSONResponse(
                status_code=401,
                content={
                    "message":
                    "Invalid token"
                },
            )

        return await call_next(
            request
        )
