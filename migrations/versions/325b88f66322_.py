"""empty message

Revision ID: 325b88f66322
Revises: dc8c1be855c
Create Date: 2015-01-10 21:28:10.493601

"""

# revision identifiers, used by Alembic.
revision = '325b88f66322'
down_revision = 'dc8c1be855c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('upgraded', sa.Boolean(), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.add_column(u'forms', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'forms', 'users', ['owner_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'forms', type_='foreignkey')
    op.drop_column(u'forms', 'owner_id')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###