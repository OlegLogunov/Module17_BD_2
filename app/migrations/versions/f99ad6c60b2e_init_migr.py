"""Init migr

Revision ID: f99ad6c60b2e
Revises: 2b3cb6f9ff96
Create Date: 2024-10-08 08:54:25.758917

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f99ad6c60b2e'
down_revision: Union[str, None] = '2b3cb6f9ff96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
