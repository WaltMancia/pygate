from datetime import (
    datetime,
    timedelta,
)


class CircuitBreaker:

    failures = {}

    opened_until = {}

    FAILURE_THRESHOLD = 5

    RECOVERY_TIMEOUT = 60

    @classmethod
    def is_open(
        cls,
        service: str,
    ):

        if service not in cls.opened_until:
            return False

        return (
            datetime.utcnow()
            < cls.opened_until[service]
        )

    @classmethod
    def record_failure(
        cls,
        service: str,
    ):

        cls.failures[service] = (
            cls.failures.get(
                service,
                0,
            )
            + 1
        )

        if (
            cls.failures[service]
            >= cls.FAILURE_THRESHOLD
        ):

            cls.opened_until[
                service
            ] = (
                datetime.utcnow()
                + timedelta(
                    seconds=cls.RECOVERY_TIMEOUT
                )
            )

    @classmethod
    def record_success(
        cls,
        service: str,
    ):

        cls.failures[service] = 0

        cls.opened_until.pop(
            service,
            None,
        )
