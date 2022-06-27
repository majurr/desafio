"""create-main-tables

Revision ID: ae7a4e693193
Revises: 
Create Date: 2022-06-22 23:00:38.157086

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = "ae7a4e693193"
down_revision = None
branch_labels = None
depends_on = None


def create_user_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("username", sa.Text, nullable=False, index=True),
        sa.Column("password", sa.Text, nullable=False),
        sa.Column("type", sa.Text, nullable=False),
        sa.Column("active", sa.Boolean, nullable=False),
    )


def upgrade() -> None:
    create_user_table()


def downgrade() -> None:
    op.drop_table("users")
