from app.db.session import (
    SessionLocal,
)

from app.models.role import (
    Role,
)

from app.models.permission import (
    Permission,
)

from app.models.role_permission import (
    RolePermission,
)

db = SessionLocal()

permissions = [

    "users.read",
    "users.create",
    "users.update",
    "users.delete",

    "routes.read",
    "routes.create",
    "routes.update",
    "routes.delete",

    "services.read",
    "services.manage",
]

for permission_name in permissions:

    existing = (
        db.query(Permission)
        .filter(
            Permission.name
            == permission_name
        )
        .first()
    )

    if not existing:

        db.add(
            Permission(
                name=permission_name
            )
        )

db.commit()

admin_role = (
    db.query(Role)
    .filter(Role.name == "admin")
    .first()
)

if not admin_role:

    admin_role = Role(
        name="admin"
    )

    db.add(admin_role)

viewer_role = (
    db.query(Role)
    .filter(Role.name == "viewer")
    .first()
)

if not viewer_role:

    viewer_role = Role(
        name="viewer"
    )

    db.add(viewer_role)

db.commit()

print("RBAC seeded")

db.close()
