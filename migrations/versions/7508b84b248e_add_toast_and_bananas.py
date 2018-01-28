"""Add toast and bananas

Revision ID: 7508b84b248e
Revises: 
Create Date: 2018-01-28 01:21:05.577259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7508b84b248e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'bananas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('color', sa.String(length=45), nullable=True),
        sa.Column('weight', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.execute("""
        INSERT INTO bananas VALUES
        (1, 'bojack', 'brown', 4.7),
        (2, 'todd', 'yellow', 3.5),
        (3, 'diane', 'green', 2.9);
    """)

    op.create_table(
        'toast',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('toastiness', sa.String(length=45), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('toast')
    op.drop_table('bananas')
