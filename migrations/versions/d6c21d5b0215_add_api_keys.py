"""add api keys

Revision ID: d6c21d5b0215
Revises: 59919be90f3b
Create Date: 2026-06-21 22:29:14.559805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6c21d5b0215'
down_revision: Union[str, Sequence[str], None] = '59919be90f3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.create_table(
        "api_keys",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
        ),

        sa.Column(
            "name",
            sa.String(100),
            nullable=False,
        ),

        sa.Column(
            "api_key",
            sa.String(255),
            nullable=False,
            unique=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
