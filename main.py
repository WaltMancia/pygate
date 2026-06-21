from app.api.routes.admin import (
    router as admin_router,
)
from fastapi import (
    FastAPI,
    Request,
)

from fastapi.responses import (
    Response,
)

from app.api.admin import (
    router as admin_router,
)

from app.core.config import (
    settings,
)

from app.core.logger import (
    configure_logging,
    logger,
)

from app.core.exceptions import (
    generic_exception_handler,
)

from app.gateway.router import (
    ROUTES,
)

from app.gateway.proxy import (
    forward_request,
)

from app.api.health import (
    router as health_router,
)

from app.api.auth import (
    router as auth_router
)

from app.middleware.auth_middleware import (
    AuthMiddleware
)

from app.api.routes.auth import (
    router as auth_router,
)

from app.middleware.rate_limit import (
    RateLimitMiddleware,
)

from app.api.routes.proxy import (
    router as proxy_router,
)

from app.middleware.request_logger import (
    RequestLoggerMiddleware,
)


configure_logging()

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(
    health_router
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

app.include_router(
    auth_router
)

app.add_middleware(
    AuthMiddleware
)

app.include_router(
    admin_router
)

app.include_router(
    auth_router
)

app.include_router(
    admin_router
)

app.add_middleware(
    RateLimitMiddleware
)

app.include_router(
    proxy_router
)

app.add_middleware(
    RequestLoggerMiddleware
)


@app.api_route(
    "/{path:path}",
    methods=[
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    ],
)
async def gateway(
    request: Request,
    path: str,
):
    logger.info(
        f"{request.method} "
        f"/{path}"
    )

    segments = path.split("/")

    first_segment = (
        "/" + segments[0]
    )

    service = ROUTES.get(
        first_segment
    )

    if not service:
        return Response(
            content="Route not found",
            status_code=404,
        )

    remaining = "/".join(
        segments[1:]
    )

    target_url = (
        f"{service}/{remaining}"
    )

    body = await request.body()

    content, status, headers = (
        await forward_request(
            target_url=target_url,
            method=request.method,
            headers=dict(
                request.headers
            ),
            body=body,
        )
    )

    return Response(
        content=content,
        status_code=status,
    )
