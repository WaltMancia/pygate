from app.core.http_client import (
    http_client,
)

from app.core.request_context import (
    current_user,
)

from starlette.requests import (
    Request,
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

    if trace_id:

        headers[
            "X-Trace-Id"
        ] = trace_id

    user = current_user.get()

    headers = headers or {}

    if user:

        headers["X-User-Id"] = str(
            user.get("sub")
        )

        headers["X-Username"] = (
            user.get("username")
        )

        headers["X-Role"] = (
            user.get("role")
        )
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

            return (
                response.status_code
                == 200
            )

        except Exception:

            return False
