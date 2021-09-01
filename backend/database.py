from typing import Optional

import settings
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine.url import URL


def get_db_url(database: Optional[str] = settings.POSTGRES_DB) -> URL:
    return URL(
        drivername="postgres",
        username=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        database=database,
    )


METADATA = MetaData()


engine = create_engine(
    get_db_url(),
    pool_size=settings.DB_CONNECTION_POOL_SIZE,
    max_overflow=settings.DB_CONNECTION_POOL_MAX_OVERFLOW,
)
