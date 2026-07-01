from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from fastapi.responses import (
    JSONResponse,
)

from app.core.route_policies import (
    ROUTE_POLICIES,
)

from app.core.security_policies import (
    SecurityPolicy,
)

from app.core.request_context import (
    current_user,
)


class AuthorizationMiddleware(
    BaseHTTPMiddleware,
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        path = request.url.path

        policy = SecurityPolicy.JWT_OR_API_KEY

        for prefix, value in ROUTE_POLICIES.items():

            if path.startswith(prefix):

                policy = value

                break

        user = current_user.get()

        if policy == SecurityPolicy.PUBLIC:

            return await call_next(
                request
            )

        if user is None:

            return JSONResponse(
                status_code=401,
                content={
                    "detail": "Authentication required"
                },
            )

        auth_type = user.get(
            "auth_type",
            "jwt",
        )

        if (
            policy == SecurityPolicy.JWT
            and auth_type != "jwt"
        ):

            return JSONResponse(
                status_code=403,
                content={
                    "detail": "JWT required"
                },
            )

        if (
            policy == SecurityPolicy.API_KEY
            and auth_type != "api_key"
        ):

            return JSONResponse(
                status_code=403,
                content={
                    "detail": "API Key required"
                },
            )

        return await call_next(
            request
        )
