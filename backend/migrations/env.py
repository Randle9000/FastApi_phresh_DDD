
import logging
from logging.config import fileConfig
import alembic

from sqlalchemy import engine_from_config, pool
from database import METADATA, get_db_url
from app import prepare

# Alembic Config object, which provides access to values within the .ini file
config = alembic.context.config

if not config.get_main_option("sqlalchemy.url"):
    DATABASE_URL = str(get_db_url())
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Interpret the config file for logging
fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = METADATA

if not target_metadata.tables:
    prepare()


def run_migrations_online() -> None:
    """
    Run migrations in 'online' mode
    """

    connectable = engine_from_config(
        config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        alembic.context.configure(
            connection=connection, target_metadata=target_metadata, transaction_per_migration=True, compare_type=True
        )

        with alembic.context.begin_transaction():
            alembic.context.run_migrations()


def run_migrations_offline() -> None:
    """
    Run migrations in 'offline' mode.
    """
    url = config.get_main_option("sqlalchemy.url")
    alembic.context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        transaction_per_migration=True,
        compare_type=True,
    )

    with alembic.context.begin_transaction():
        alembic.context.run_migrations()


if alembic.context.is_offline_mode():
    logger.info("Running migrations offline")
    run_migrations_offline()
else:
    logger.info("Running migrations online")
    run_migrations_online()
