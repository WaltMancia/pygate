from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.repositories.gateway_analytics_repository import (
    GatewayAnalyticsRepository,
)

from app.services.gateway_analytics_service import (
    GatewayAnalyticsService,
)


def get_gateway_analytics_service(
    db: Session = Depends(get_db),
):

    repository = GatewayAnalyticsRepository(
        db
    )

    return GatewayAnalyticsService(
        repository
    )
