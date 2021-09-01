import abc
from typing import List
from domain.base import BaseDto
from domain.types import CleaningID


class CleaningDataDto(BaseDto):
    id: CleaningID
    name: str
    description: str
    cleaning_type: str
    price: int


class CleaningSelector(abc.ABC):
    @abc.abstractmethod
    def get_cleaning_data(self, cleaning_id: CleaningID) -> CleaningDataDto:
        ...

    @abc.abstractmethod
    def get_all_cleanings(self) -> List[CleaningDataDto]:
        ...
