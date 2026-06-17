from fastapi import (
    Depends,
    HTTPException,
)

from app.api.dependencies.auth import (
    get_current_user,
)


def require_role(
    role_name: str,
):

    def checker(
        current_user=Depends(
            get_current_user
        )
    ):

        if (
            current_user.role.name
            != role_name
        ):
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        return current_user

    return checker
