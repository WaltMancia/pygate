from app.models.gateway_analytics import (
    GatewayAnalytics,
)

from app.repositories.gateway_analytics_repository import (
    GatewayAnalyticsRepository,
)


class GatewayAnalyticsService:

    def __init__(
        self,
        repository: GatewayAnalyticsRepository,
    ):
        self.repository = repository

    def register(
        self,
        **kwargs,
    ):

        analytics = GatewayAnalytics(
            **kwargs,
        )

        self.repository.save(
            analytics
        )

    def summary(
        self,
    ):

        return {
            "requests":
                self.repository.total_requests(),

            "average_latency":
                self.repository.average_latency(),

            "top_endpoints":
                self.repository.top_endpoints(),
        }
