from fastapi import (
    APIRouter,
)

from fastapi.responses import (
    PlainTextResponse,
)

from prometheus_client import (
    generate_latest,
)

router = APIRouter(
    prefix="/prometheus",
    tags=["Prometheus"],
)


@router.get(
    "",
    response_class=PlainTextResponse,
)
def prometheus_metrics():

    return generate_latest()