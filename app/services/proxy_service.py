from app.core.http_client import (
    http_client,
)


class ProxyService:

    @staticmethod
    async def get(
        url: str,
    ):

        response = (
            await http_client.get(
                url
            )
        )

        return response
