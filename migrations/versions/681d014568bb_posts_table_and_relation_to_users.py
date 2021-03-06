"""posts table and relation to users

Revision ID: 681d014568bb
Revises: 81aaa04f940c
Create Date: 2021-07-04 18:53:36.432294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '681d014568bb'
down_revision = '81aaa04f940c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_created'), 'post', ['created'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_created'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
