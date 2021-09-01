from typing import cast

from domain.cleanings.models import Cleaning
from domain.cleanings.repositories import CleaningRepository
from domain.types import CleaningID
from fastapi_sqlalchemy import db


class SqlAlchemyCleaningRepository(CleaningRepository):
    def add(self, instance: Cleaning) -> None:
        db.session.add(instance)
        db.session.flush()

    # TODO add methods to not found, as decorator
    def get_by_id(self, id: CleaningID) -> Cleaning:
        return cast(Cleaning, db.session.query(Cleaning).filter(Cleaning.id == id).one())

    def update(self, instance: Cleaning) -> None:
        db.session.add(instance=instance)
        db.session.flush()
