"""create_main_tables

Revision ID: fcf693f61018
Revises:
Create Date: 2021-01-16 17:12:20.667046

"""
from typing import Tuple

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic
revision = "fcf693f61018"
down_revision = None
branch_labels = None
depends_on = None


def create_updated_at_trigger() -> None:
    """
    We've also written a PL/pgSQL trigger that we create for every table in our create_updated_at_trigger function.
    This trigger will run whenever a row in a given table is updated and set the updated_at column
    to that moment in time. Handing the management of updating timestamps over to postgres is relatively
    straightforward and extremely convenient in the long run
    https://www.postgresql.org/docs/12/plpgsql-overview.html
    """
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
            RETURNS TRIGGER AS
        $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """
    )


def timestamps(indexed: bool = False) -> Tuple[sa.Column, sa.Column]:
    """
    Method which created two timestamp columns. In this way it will be easier to add them to other tables

    """
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
    )


def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        # should be? :         sa.Column("id", postgresql.UUID(as_uuid=False), nullable=False),
        sa.Column("id", sa.Text, nullable=False),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        # sa.Column("owner", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE")),
        # *timestamps(),
    )
    # op.execute(
    #     """
    #     CREATE TRIGGER update_cleanings_modtime
    #         BEFORE UPDATE
    #         ON cleanings
    #         FOR EACH ROW
    #     EXECUTE PROCEDURE update_updated_at_column();
    #     """
    # )


def create_users_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("email", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("email_verified", sa.Boolean, nullable=False, server_default="False"),
        sa.Column("salt", sa.Text, nullable=False),
        sa.Column("password", sa.Text, nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="True"),
        sa.Column("is_superuser", sa.Boolean(), nullable=False, server_default="False"),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_user_modtime
            BEFORE UPDATE
            ON users
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_profiles_table() -> None:
    op.create_table(
        "profiles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("full_name", sa.Text, nullable=True),
        sa.Column("phone_number", sa.Text, nullable=True),
        sa.Column("bio", sa.Text, nullable=True, server_default=""),
        sa.Column("image", sa.Text, nullable=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE")),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_profiles_modtime
            BEFORE UPDATE
            ON profiles
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


# the order of function calls in the 'upgrade' matters
def upgrade() -> None:
    # create_updated_at_trigger()
    # create_users_table()
    # create_profiles_table()
    create_cleanings_table()


def downgrade() -> None:
    op.drop_table("cleanings")
    # op.drop_table("profiles")
    # op.drop_table("users")
    # op.execute("DROP FUNCTION update_updated_at_column")
