"""table

Revision ID: 80fd52938e9c
Revises: 
Create Date: 2021-06-06 18:50:44.201172

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '80fd52938e9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'auth',
        sa.Column(
            'id', postgresql.UUID(), autoincrement=False, nullable=False
        ),
        sa.Column(
            'user_email', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True
        ),
        sa.Column('token', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column(
            'refresh_token', sa.VARCHAR(), autoincrement=False, nullable=True
        ),
        sa.Column(
            'client_id', sa.VARCHAR(), autoincrement=False, nullable=True
        ),
        sa.Column(
            'client_secret', sa.VARCHAR(), autoincrement=False, nullable=True
        ),
        sa.Column('expiry', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='auth_pkey')
    )


def downgrade():
    op.drop_table('auth')
