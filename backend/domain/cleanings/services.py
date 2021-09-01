import dataclasses
from typing import Optional

from domain.base import BaseDto
from domain.cleanings.const import CleaningType
from domain.cleanings.models import Cleaning
from domain.cleanings.repositories import CleaningRepository
from domain.cleanings.selectors import CleaningSelector
from domain.types import CleaningID
from domain.cleanings.const import CleaningType


class CreateCleaningDto(BaseDto):
    name: str
    description: str
    price: int
    cleaning_type: Optional[CleaningType]


class UpdateCleaningDto(BaseDto):
    name: Optional[str]
    description: Optional[str]
    price: Optional[int]
    cleaning_type: Optional[CleaningType]


@dataclasses.dataclass  # TODO why not as static class ?
class CleaningService:
    cleaning_repository: CleaningRepository
    cleaning_selector: CleaningSelector

    # TODO why not static or class method ?
    def create_cleaning(self, dto: CreateCleaningDto) -> CleaningID:
        cleaning = Cleaning.create_new(
            name=dto.name,
            description=dto.name,
            price=dto.price,
            cleaning_type=dto.cleaning_type,
        )
        self.cleaning_repository.add(cleaning)

        return cleaning.id

    def update_cleaning(self, cleaning_id, dto):
        cleaning = self.cleaning_repository.get_by_id(id=cleaning_id)

        if not cleaning:
            return None

        for k, v in dto.__dict__.items():
            try:
                if k == "cleaning_type":
                    v = CleaningType(dto.__getattribute__(k))
                    print(v)
                cleaning.__setattr__(k, v)
            except KeyError as e:
                return None # TODO raise specific Http Error

        self.cleaning_repository.add(cleaning)

        return self.cleaning_selector.get_cleaning_data(cleaning_id=cleaning_id)














