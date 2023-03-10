"""update project

Revision ID: fec019fa3432
Revises: 60c57cd33b1a
Create Date: 2023-01-19 04:42:41.448284

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fec019fa3432'
down_revision = '60c57cd33b1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', mysql.DATETIME(), nullable=True))

    # ### end Alembic commands ###
