"""upload avatar

Revision ID: 7116e5dc36d0
Revises: 896644b72293
Create Date: 2021-12-08 20:13:33.749428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7116e5dc36d0'
down_revision = '896644b72293'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_avatar')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_avatar', sa.BLOB(), nullable=True))
    # ### end Alembic commands ###
