"""empty message

Revision ID: de345335c6c4
Revises: 
Create Date: 2023-03-30 14:14:15.569735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de345335c6c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('usuario_nome', sa.String(length=80), nullable=False),
    sa.Column('usuario_email', sa.String(length=120), nullable=False),
    sa.Column('usuario_password', sa.String(length=100), nullable=False),
    sa.Column('usuario_is_authenticated', sa.Integer(), nullable=False),
    sa.Column('usuario_status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('usuario_id'),
    sa.UniqueConstraint('usuario_email'),
    sa.UniqueConstraint('usuario_nome')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
