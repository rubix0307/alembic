"""edit_names

Revision ID: 95554460b67f
Revises: 2ea356058839
Create Date: 2023-08-19 20:42:05.357095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '95554460b67f'
down_revision: Union[str, None] = '2ea356058839'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=255), nullable=True))
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255), nullable=True))
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
