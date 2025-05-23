"""empty message

Revision ID: d7a42a374a44
Revises: 2d484971bd96
Create Date: 2025-03-20 07:25:51.961531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7a42a374a44'
down_revision = '2d484971bd96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('e_id', sa.Integer(), nullable=False),
    sa.Column('s_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['e_id'], ['employee.employee_id'], ),
    sa.ForeignKeyConstraint(['s_id'], ['services.id'], ),
    sa.ForeignKeyConstraint(['u_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    # ### end Alembic commands ###
