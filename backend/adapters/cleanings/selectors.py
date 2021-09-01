from domain.cleanings.models import Cleaning
from domain.cleanings.selectors import CleaningDataDto, CleaningSelector
from domain.types import CleaningID
from fastapi_sqlalchemy import db
from typing import List


class SqlAlchemyCleaningSelector(CleaningSelector):
    def get_cleaning_data(self, cleaning_id: CleaningID) -> CleaningDataDto:
        cleaning = db.session.query(Cleaning).filter(Cleaning.id == cleaning_id).one()

        return CleaningDataDto(
            id=cleaning.id,
            name=cleaning.name,
            description=cleaning.description,
            cleaning_type=cleaning.cleaning_type,
            price=cleaning.price,
        )

    def get_all_cleanings(self) -> List[CleaningDataDto]:
        cleanings = db.session.query(Cleaning).all()
        cleanings_dto = []
        for cleaning in cleanings:
            cleaning_dto = CleaningDataDto(
                id=cleaning.id,
                name=cleaning.name,
                description=cleaning.description,
                cleaning_type=cleaning.cleaning_type,
                price=cleaning.price,
            )
            cleanings_dto.append(cleaning_dto)
        return cleanings_dto
