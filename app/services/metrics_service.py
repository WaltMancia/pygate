from app.core.prometheus import (
    REQUEST_COUNTER,
    CACHE_HITS,
    CACHE_MISSES,
)


class MetricsService:

    requests = 0

    proxied_requests = 0

    cache_hits = 0

    cache_misses = 0

    @classmethod
    def increment_requests(
        cls,
    ):
        cls.requests += 1

    @classmethod
    def increment_proxied(
        cls,
    ):
        cls.proxied_requests += 1

    @classmethod
    def increment_cache_hit(
        cls,
    ):
        cls.cache_hits += 1

    @classmethod
    def increment_cache_miss(
        cls,
    ):
        cls.cache_misses += 1
