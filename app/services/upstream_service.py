from app.core.upstreams import (
    UPSTREAM_SERVICES,
)


class UpstreamServiceManager:

    @staticmethod
    def get_service(
        service_name: str,
    ):

        return (
            UPSTREAM_SERVICES.get(
                service_name
            )
        )

    @staticmethod
    def list_services():

        return (
            UPSTREAM_SERVICES
        )
