from fastapi import (
    APIRouter,
    Depends,
)

from app.api.dependencies.analytics import (
    get_gateway_analytics_service,
)

from app.services.gateway_analytics_service import (
    GatewayAnalyticsService,
)

router = APIRouter(
    prefix="/admin/analytics",
    tags=["Analytics"],
)


@router.get(
    "/summary",
)
def summary(
    service: GatewayAnalyticsService = Depends(
        get_gateway_analytics_service
    ),
):

    return service.summary()
