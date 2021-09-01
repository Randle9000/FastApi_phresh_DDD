from typing import cast

from adapters.cleanings.repositories import SqlAlchemyCleaningRepository
from adapters.cleanings.selectors import SqlAlchemyCleaningSelector
from dependencies import Injector
from domain.cleanings.repositories import CleaningRepository
from domain.cleanings.selectors import CleaningSelector


class AdaptersContainer(Injector):
    cleaning_repository = cast(CleaningRepository, SqlAlchemyCleaningRepository)
    cleaning_selector = cast(CleaningSelector, SqlAlchemyCleaningSelector)
