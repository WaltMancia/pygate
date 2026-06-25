from prometheus_client import (
    Counter,
)

REQUEST_COUNTER = Counter(
    "gateway_requests_total",
    "Total requests",
)

CACHE_HITS = Counter(
    "gateway_cache_hits_total",
    "Cache hits",
)

CACHE_MISSES = Counter(
    "gateway_cache_misses_total",
    "Cache misses",
)
