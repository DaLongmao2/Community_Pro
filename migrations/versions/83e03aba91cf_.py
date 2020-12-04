"""empty message

Revision ID: 83e03aba91cf
Revises: 0a6108af9ff9
Create Date: 2020-12-04 08:53:43.463903

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '83e03aba91cf'
down_revision = '0a6108af9ff9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###
