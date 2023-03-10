"""create table client

Revision ID: 42bd1ec2367d
Revises: 
Create Date: 2023-01-18 13:11:49.645676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42bd1ec2367d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('client_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('client_name', sa.String(length=250), nullable=False),
    sa.Column('client_address', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('client_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client')
    # ### end Alembic commands ###
