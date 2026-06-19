from collections import defaultdict

from app.core.upstreams import (
    UPSTREAM_SERVICES,
)


class RoundRobinBalancer:

    _indexes = defaultdict(int)

    @classmethod
    def next_instance(
        cls,
        service_name: str,
    ):

        instances = (
            UPSTREAM_SERVICES.get(
                service_name
            )
        )

        if not instances:

            return None

        index = (
            cls._indexes[
                service_name
            ]
        )

        selected = (
            instances[
                index %
                len(instances)
            ]
        )

        cls._indexes[
            service_name
        ] += 1

        return selected
