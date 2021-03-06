"""empty message

Revision ID: 44b0e2a6aa5
Revises: None
Create Date: 2014-11-12 20:13:35.824891

"""

# revision identifiers, used by Alembic.
revision = '44b0e2a6aa5'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('intro', sa.String(length=254), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=254), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogs')
    op.drop_table('users')
    op.drop_table('types')
    ### end Alembic commands ###
