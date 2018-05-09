"""20180508

Revision ID: 156bdd29e989
Revises: 
Create Date: 2018-05-08 20:19:12.819952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '156bdd29e989'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('picture', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'picture')
    # ### end Alembic commands ###
