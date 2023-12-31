"""empty message

Revision ID: b1279059c1e1
Revises: b260d984d221
Create Date: 2023-10-01 10:47:05.129702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1279059c1e1'
down_revision = 'b260d984d221'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.String(length=200), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_item', schema=None) as batch_op:
        batch_op.drop_column('price')

    # ### end Alembic commands ###
