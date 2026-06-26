from app.core.http_client import (
    http_client,
)

from app.core.request_context import (
    current_user,
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

            if user.get("sub") is not None:
                headers["X-User-Id"] = str(
                    user.get("sub")
                )

            if user.get("username"):
                headers["X-Username"] = user.get(
                    "username"
                )

            if user.get("role"):
                headers["X-Role"] = user.get(
                    "role"
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
