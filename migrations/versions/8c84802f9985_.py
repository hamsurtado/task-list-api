"""empty message

Revision ID: 8c84802f9985
Revises: 6798d5af6dbb
Create Date: 2023-05-08 15:31:23.494213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c84802f9985'
down_revision = '6798d5af6dbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('task', 'task_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('task_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('task', 'id')
    # ### end Alembic commands ###
