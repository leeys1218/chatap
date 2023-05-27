"""empty message

Revision ID: 9b3ef299645b
Revises: b973507bf5e8
Create Date: 2023-05-19 13:30:20.135291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b3ef299645b'
down_revision = 'b973507bf5e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('create_date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'create_date')
    # ### end Alembic commands ###
