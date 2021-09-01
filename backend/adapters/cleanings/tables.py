from database import METADATA
from domain.cleanings.models import Cleaning
from sqlalchemy import Column, Numeric, String, Table, Text
from sqlalchemy.orm import mapper

CLEANING_TABLE = Table(
    "cleanings",
    METADATA,
    Column("id", String(10), primary_key=True),
    Column("name", Text, nullable=False, index=True),
    Column("description", Text, nullable=False),
    Column("cleaning_type", Text, nullable=False),
    Column("price", Numeric(10, 2), nullable=False),
)


mapper(Cleaning, CLEANING_TABLE)
