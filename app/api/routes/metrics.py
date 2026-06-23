from fastapi import (
    APIRouter,
)

from app.services.metrics_service import (
    MetricsService,
)

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)


@router.get("")
def metrics():

    return {
        "requests":
            MetricsService.requests,

        "proxied_requests":
            MetricsService.proxied_requests,

        "cache_hits":
            MetricsService.cache_hits,

        "cache_misses":
            MetricsService.cache_misses,
    }
