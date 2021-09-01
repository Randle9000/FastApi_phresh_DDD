from databases import DatabaseURL  # should work in docker it's not installed locally
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".envs/.local.env")

PROJECT_NAME = "phresh"
VERSION = "0.0.1"
API_PREFIX = "/api"

SECRET_KEY = config("SECRET_KEY", cast=Secret)
ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=7 * 24 * 60  # one week
)

POSTGRES_HOST = config("POSTGRES_HOST", cast=str)
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default=5432)
POSTGRES_DB = config("POSTGRES_DB", cast=str)
POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")

DB_CONNECTION_POOL_SIZE = config("DB_CONNECTION_POOL_SIZE", default=10)
DB_CONNECTION_POOL_MAX_OVERFLOW = config("DB_CONNECTION_POOL_MAX_OVERFLOW", default=20)

# DATABASE_URL = config(
#     "DATABASE_URL",
#     cast=DatabaseURL,
#     default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}",
# )
