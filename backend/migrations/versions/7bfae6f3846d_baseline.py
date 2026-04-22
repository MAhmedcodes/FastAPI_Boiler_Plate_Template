"""baseline

Revision ID: 7bfae6f3846d
Revises: 
Create Date: 2026-04-22 11:41:03.957602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bfae6f3846d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create organizations table
    op.create_table(
        'organizations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('invite_token', sa.String(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
        sa.UniqueConstraint('invite_token')
    )

    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False),
        sa.Column('oauth_provider', sa.String(), nullable=True),
        sa.Column('oauth_id', sa.String(), nullable=True),
        sa.Column('is_verified', sa.Boolean(),
                  server_default=sa.text('false'), nullable=False),
        sa.Column('last_login', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('organization_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email', 'organization_id',
                            name='unique_email_per_organization')
    )

    # Create otps table
    op.create_table(
        'otps',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('otp_code', sa.String(6), nullable=False),
        sa.Column('expires_at', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('is_used', sa.Boolean(),
                  server_default=sa.text('false'), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Create task_controls table
    op.create_table(
        'task_controls',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('task_name', sa.String(), nullable=False),
        sa.Column('is_paused', sa.Boolean(),
                  server_default=sa.text('false'), nullable=False),
        sa.Column('paused_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), onupdate=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('task_name')
    )

    # Add foreign key constraints
    op.create_foreign_key('fk_otps_user_id', 'otps', 'users', [
                          'user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_users_organization_id', 'users', 'organizations', [
                          'organization_id'], ['id'], ondelete='CASCADE')


def downgrade() -> None:
    # Drop foreign keys
    op.drop_constraint('fk_otps_user_id', 'otps', type_='foreignkey')
    op.drop_constraint('fk_users_organization_id', 'users', type_='foreignkey')

    # Drop tables in reverse order
    op.drop_table('task_controls')
    op.drop_table('otps')
    op.drop_table('users')
    op.drop_table('organizations')
