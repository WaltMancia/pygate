from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_by_username(
        self,
        username: str,
    ):
        return (
            self.db.query(User)
            .filter(
                User.username == username
            )
            .first()
        )

    def create(
        self,
        username: str,
        password_hash: str,
        role_id: int,
    ):

        user = User(
            username=username,
            password_hash=password_hash,
            role_id=role_id,
        )

        self.db.add(user)

        self.db.commit()

        self.db.refresh(user)

        return user
