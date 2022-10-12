"""empty message

Revision ID: f80d6a743e1f
Revises: dae5a1f49930
Create Date: 2022-10-06 20:21:51.271339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f80d6a743e1f'
down_revision = 'dae5a1f49930'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
