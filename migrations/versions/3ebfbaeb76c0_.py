"""empty message

Revision ID: 3ebfbaeb76c0
Revises: 0a89c670fc7a
Create Date: 2019-11-18 19:29:43.277973

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ebfbaeb76c0'
down_revision = '0a89c670fc7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_change',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('new_email', sa.String(length=128), nullable=False),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('expired', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('new_email')
    )
    op.create_index(op.f('ix_email_change_user_id'), 'email_change', ['user_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_email_change_user_id'), table_name='email_change')
    op.drop_table('email_change')
    # ### end Alembic commands ###
