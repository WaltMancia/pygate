from app.core.security_policies import (
    SecurityPolicy,
)

ROUTE_POLICIES = {

    "/auth/login":
        SecurityPolicy.PUBLIC,

    "/health":
        SecurityPolicy.PUBLIC,

    "/metrics":
        SecurityPolicy.PUBLIC,

    "/admin":
        SecurityPolicy.JWT,

    "/internal":
        SecurityPolicy.API_KEY,

    "/api":
        SecurityPolicy.JWT_OR_API_KEY,
}
