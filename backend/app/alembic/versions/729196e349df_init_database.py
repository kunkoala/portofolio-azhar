"""init database

Revision ID: 729196e349df
Revises: b9b0bc35d72f
Create Date: 2024-07-27 23:13:17.861164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '729196e349df'
down_revision: Union[str, None] = 'b9b0bc35d72f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
