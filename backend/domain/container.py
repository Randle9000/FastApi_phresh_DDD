from typing import cast

from dependencies import Injector
from domain.cleanings.services import CleaningService


class DomainContainer(Injector):
    cleaning_service = cast(CleaningService, CleaningService)
