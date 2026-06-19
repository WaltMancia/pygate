from collections import defaultdict

from app.services.service_registry import (
    ServiceRegistry,
)


class RoundRobinBalancer:

    _indexes = defaultdict(int)

    @classmethod
    def next_instance(
        cls,
        service_name: str,
    ):

        instances = (
            ServiceRegistry
            .get_instances(
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
