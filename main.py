from fastapi import FastAPI

from app.core.config import (
    settings,
)

from app.middleware.authorization import (
    AuthorizationMiddleware,
)

from app.core.logger import (
    configure_logging,
)

from app.core.exceptions import (
    generic_exception_handler,
)

from app.middleware.request_logger import (
    RequestLoggerMiddleware,
)

from app.middleware.rate_limit import (
    RateLimitMiddleware,
)

from app.api.routes.auth import (
    router as auth_router,
)

from app.api.routes.proxy import (
    router as proxy_router,
)

from app.api.routes.admin import (
    router as admin_router,
)

from app.api.routes.metrics import (
    router as metrics_router,
)

from app.api.routes.health import (
    router as health_router,
)

from app.api.routes.prometheus import (
    router as prometheus_router,
)

from app.api.routes.api_keys import (
    router as api_key_router,
)

from app.middleware.api_key_auth import (
    ApiKeyAuthMiddleware,
)

from app.api.routes.analytics import (
    router as analytics_router,
)

configure_logging()

app = FastAPI(
    title=settings.APP_NAME,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

app.add_middleware(
    RequestLoggerMiddleware,
)

app.add_middleware(
    RateLimitMiddleware,
)

app.include_router(
    health_router,
)

app.include_router(
    auth_router,
)

app.include_router(
    proxy_router,
)

app.include_router(
    admin_router,
)

app.include_router(
    metrics_router,
)

app.include_router(
    prometheus_router,
)
app.include_router(
    api_key_router
)

app.add_middleware(
    ApiKeyAuthMiddleware,
)

app.add_middleware(
    RequestLoggerMiddleware,
)

app.add_middleware(
    RateLimitMiddleware,
)

app.add_middleware(
    AuthorizationMiddleware,
)

app.include_router(
    analytics_router
)
