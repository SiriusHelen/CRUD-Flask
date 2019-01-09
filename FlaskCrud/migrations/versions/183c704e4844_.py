"""empty message

Revision ID: 183c704e4844
Revises: 6fde08634266
Create Date: 2018-12-27 23:30:00.335528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183c704e4844'
down_revision = '6fde08634266'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'Websitedetails', 'users', ['uid'], ['uid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Websitedetails', type_='foreignkey')
    # ### end Alembic commands ###
