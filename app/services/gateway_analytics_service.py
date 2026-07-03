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
                round(
                    self.repository.average_latency(),
                    2,
                ),

            "errors":
                self.repository.total_errors(),

            "top_endpoints":
                self.repository.top_endpoints(),

            "services":
                self.repository.requests_by_service(),
        }
