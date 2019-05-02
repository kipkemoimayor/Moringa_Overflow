"""Innitial migration

Revision ID: 269af9a6ddfd
Revises: 
Create Date: 2019-05-01 22:06:12.295190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '269af9a6ddfd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###
