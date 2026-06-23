import time
import uuid

from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from app.core.logger import (
    logger,
)


class RequestLoggerMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        trace_id = str(
            uuid.uuid4()
        )

        start = time.time()

        response = await call_next(
            request
        )

        duration = round(
            (
                time.time()
                - start
            )
            * 1000,
            2,
        )

        logger.info(
            {
                "trace_id": trace_id,
                "method": request.method,
                "path": request.url.path,
                "status": response.status_code,
                "latency_ms": duration,
                "client_ip": request.client.host,
            }
        )

        response.headers[
            "X-Trace-Id"
        ] = trace_id

        return response
