"""add comment to student

Revision ID: 148fa3c96f75
Revises: 
Create Date: 2024-01-07 13:21:40.569454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '148fa3c96f75'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('student') as batch_op:
        batch_op.add_column(sa.Column("comment", sa.String))


def downgrade() -> None:
    with op.batch_alter_table('student') as batch_op:
        batch_op.drop_column(sa.Column("comment", sa.String))
