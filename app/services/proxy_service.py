from app.core.http_client import (
    http_client,
)

from app.core.request_context import (
    current_user,
)

import time

from app.db.session import (
    SessionLocal,
)

from app.repositories.gateway_analytics_repository import (
    GatewayAnalyticsRepository,
)

from app.services.gateway_analytics_service import (
    GatewayAnalyticsService,
)


class ProxyService:

    @staticmethod
    async def forward(
        method: str,
        url: str,
        headers=None,
        body=None,
        trace_id=None,
    ):

        headers = headers or {}

        user = current_user.get()

        if user:

            auth_type = user.get(
                "auth_type",
                "jwt",
            )

            headers["X-Auth-Type"] = auth_type

            if auth_type == "api_key":

                headers["X-Api-Owner"] = user.get(
                    "owner"
                )

            else:

                if user.get("sub"):

                    headers["X-User-Id"] = str(
                        user["sub"]
                    )

                if user.get("username"):

                    headers["X-Username"] = (
                        user["username"]
                    )

                if user.get("role"):

                    headers["X-Role"] = (
                        user["role"]
                    )

        if trace_id:
            headers["X-Trace-Id"] = trace_id

        response = await http_client.request(
            method=method,
            url=url,
            headers=headers,
            content=body,
        )

        return response

    @staticmethod
    async def health_check(
        url: str,
    ):

        try:

            response = await http_client.get(
                f"{url}/health"
            )

            return response.status_code == 200

        except Exception:

            return False
