from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.gateway_analytics import (
    GatewayAnalytics,
)


class GatewayAnalyticsRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def save(
        self,
        analytics: GatewayAnalytics,
    ):

        self.db.add(analytics)

        self.db.commit()

    def total_requests(
        self,
    ):

        return (
            self.db.query(
                GatewayAnalytics
            )
            .count()
        )

    def average_latency(
        self,
    ):

        value = (
            self.db.query(
                func.avg(
                    GatewayAnalytics.latency
                )
            )
            .scalar()
        )

        return value or 0

    def top_endpoints(
        self,
        limit: int = 5,
    ):

        return (
            self.db.query(
                GatewayAnalytics.endpoint,
                func.count().label(
                    "total"
                ),
            )
            .group_by(
                GatewayAnalytics.endpoint
            )
            .order_by(
                func.count().desc()
            )
            .limit(limit)
            .all()
        )
