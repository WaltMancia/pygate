from app.core.upstreams import (
    UPSTREAM_SERVICES,
)

from app.services.load_balancer import (
    RoundRobinBalancer,
)


class UpstreamServiceManager:

    @staticmethod
    def get_service(
        service_name: str,
    ):

        return (
            RoundRobinBalancer
            .next_instance(
                service_name
            )
        )

    @staticmethod
    def list_services():

        return (
            UPSTREAM_SERVICES
        )
