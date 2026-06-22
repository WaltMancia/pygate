from app.core.http_client import (
    http_client,
)


class ProxyService:

    @staticmethod
    async def forward(
        method: str,
        url: str,
        headers=None,
        body=None,
    ):

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
