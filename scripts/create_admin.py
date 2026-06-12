from app.db.session import (
    SessionLocal,
)

from app.repositories.user_repository import (
    UserRepository,
)

from app.core.passwords import (
    hash_password,
)

db = SessionLocal()

repo = UserRepository(db)

existing = repo.get_by_username(
    "admin"
)

if existing:

    print(
        "Admin already exists"
    )

else:

    repo.create(
        username="admin",
        password_hash=hash_password(
            "Admin123!"
        ),
        role="admin",
    )

    print(
        "Admin created"
    )

db.close()
