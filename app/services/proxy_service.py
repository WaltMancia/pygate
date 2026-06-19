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

    @staticmethod
    async def health_check(
        url: str,
    ):

        try:

            response = (
                await http_client.get(
                    f"{url}/health"
                )
            )

            return (
                response.status_code
                == 200
            )

        except Exception:

            return False
