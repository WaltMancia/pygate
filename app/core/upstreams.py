from app.services.service_registry import (
    ServiceRegistry,
)

UPSTREAM_SERVICES = {
    "users": [
        "http://localhost:8001",
        "http://localhost:8004",
        "http://localhost:8005",
    ],
    "products": [
        "http://localhost:8002",
    ],
    "orders": [
        "http://localhost:8003",
    ],
}

for (
    service,
    instances
) in (
    UPSTREAM_SERVICES.items()
):

    ServiceRegistry.set_health(
        service,
        instances,
    )
