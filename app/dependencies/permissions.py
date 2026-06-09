from fastapi import (
    Request,
    HTTPException,
)


def require_permission(
    permission: str,
):

    async def checker(
        request: Request,
    ):

        user = request.state.user

        permissions = (
            user.get(
                "permissions",
                [],
            )
        )

        if permission not in permissions:

            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        return True

    return checker
