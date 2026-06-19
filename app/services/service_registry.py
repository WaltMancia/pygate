class ServiceRegistry:

    healthy_instances = {}

    @classmethod
    def set_health(
        cls,
        service,
        instances,
    ):

        cls.healthy_instances[
            service
        ] = instances

    @classmethod
    def get_instances(
        cls,
        service,
    ):

        return (
            cls.healthy_instances.get(
                service,
                [],
            )
        )
