import httpx


async def forward_request(
    target_url: str,
    method: str,
    headers: dict,
    body: bytes,
):
    async with httpx.AsyncClient(
        timeout=30
    ) as client:

        response = (
            await client.request(
                method=method,
                url=target_url,
                headers=headers,
                content=body,
            )
        )

        return (
            response.content,
            response.status_code,
            response.headers,
        )
