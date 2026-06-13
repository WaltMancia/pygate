from app.db.session import (
    SessionLocal,
)

from app.repositories.user_repository import (
    UserRepository,
)

from app.models.role import (
    Role,
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

    admin_role = (
        db.query(Role)
        .filter(
            Role.name == "admin"
        )
        .first()
    )

    if not admin_role:

        print(
            "Admin role not found. Run seed_rbac first."
        )

    else:

        repo.create(
            username="admin",
            password_hash=hash_password(
                "Admin123!"
            ),
            role_id=admin_role.id,
        )

        print(
            "Admin created"
        )

db.close()
