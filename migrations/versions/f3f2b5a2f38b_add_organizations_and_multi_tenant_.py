"""add organizations and multi-tenant support

Revision ID: f3f2b5a2f38b
Revises: a7048a8e06ad
Create Date: 2026-04-15 15:46:48.032833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3f2b5a2f38b'
down_revision: Union[str, Sequence[str], None] = 'a7048a8e06ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Create organizations table
    op.create_table('organizations',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )

    # 2. Add organization_id as nullable first
    op.add_column('users', sa.Column(
        'organization_id', sa.Integer(), nullable=True))

    # 3. Insert default organization
    op.execute("INSERT INTO organizations (name) VALUES ('default')")

    # 4. Update existing users to default organization
    op.execute("UPDATE users SET organization_id = (SELECT id FROM organizations WHERE name = 'default') WHERE organization_id IS NULL")

    # 5. Now alter the column to be NOT NULL
    op.alter_column('users', 'organization_id',
                    existing_type=sa.Integer(), nullable=False)

    # 6. Create foreign key constraint
    op.create_foreign_key('fk_users_organization_id', 'users', 'organizations', [
                          'organization_id'], ['id'], ondelete='CASCADE')

    # 7. Remove old unique constraint on email
    op.drop_constraint('users_email_key', 'users', type_='unique')

    # 8. Add new composite unique constraint
    op.create_unique_constraint('unique_email_per_organization', 'users', [
                                'email', 'organization_id'])


def downgrade() -> None:
    # 1. Drop composite unique constraint
    op.drop_constraint('unique_email_per_organization',
                       'users', type_='unique')

    # 2. Re-add old unique constraint on email
    op.create_unique_constraint('users_email_key', 'users', ['email'])

    # 3. Drop foreign key constraint
    op.drop_constraint('fk_users_organization_id', 'users', type_='foreignkey')

    # 4. Drop organization_id column
    op.drop_column('users', 'organization_id')

    # 5. Drop organizations table
    op.drop_table('organizations')
