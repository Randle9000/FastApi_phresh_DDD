import abc

from domain.cleanings.models import Cleaning
from domain.types import CleaningID


class CleaningRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, instance: Cleaning) -> None:
        ...

    @abc.abstractmethod
    def get_by_id(self, id: CleaningID) -> Cleaning:
        ...

    @abc.abstractmethod
    def update(self, instance: Cleaning) -> None:
        ...
