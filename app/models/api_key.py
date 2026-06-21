from sqlalchemy import (
    Integer,
    String,
)

from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)

from app.db.base import Base


class ApiKey(Base):

    __tablename__ = "api_keys"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    api_key: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )
