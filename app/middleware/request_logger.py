from starlette.middleware.base import (
    BaseHTTPMiddleware,
)
import uuid
import time
request_logger.py


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

        print(
            f"[{trace_id}] "
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{duration}ms"
        )

        response.headers[
            "X-Trace-Id"
        ] = trace_id

        return response
