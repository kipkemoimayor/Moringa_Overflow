"""empty message

Revision ID: 22f335ce1e50
Revises: 4e66839fc88f
Create Date: 2019-05-02 12:32:34.888095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f335ce1e50'
down_revision = '4e66839fc88f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('votes_userid', sa.Integer(), nullable=True),
    sa.Column('ans_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ans_id'], ['answers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('answers', 'votes_userid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('votes_userid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_table('votes')
    # ### end Alembic commands ###