from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.repositories.api_key_repository import (
    ApiKeyRepository,
)

from app.core.request_context import (
    current_user,
)


class ApiKeyAuthMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        api_key = request.headers.get(
            "X-API-Key"
        )

        if api_key:

            db: Session = SessionLocal()

            try:

                repository = ApiKeyRepository(
                    db
                )

                key = repository.get_by_key(
                    api_key
                )

                if key:

                    current_user.set(
                        {
                            "owner": key.owner,
                            "auth_type": "api_key",
                        }
                    )

            finally:

                db.close()

        return await call_next(
            request
        )
