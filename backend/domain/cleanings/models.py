from __future__ import annotations

import dataclasses
from typing import Optional

from domain.cleanings.const import CleaningType
from domain.types import CleaningID


@dataclasses.dataclass(eq=False)
class Cleaning:  # in homies it inherits from abstract class Entity
    id: CleaningID
    name: str
    description: str
    price: int
    cleaning_type: Optional[CleaningType]

    @classmethod
    def next_id(cls) -> CleaningID:
        # TODO to fix, here it's just to learn purposes
        import secrets
        import string

        alphabet = string.ascii_uppercase + string.digits
        return CleaningID("".join(secrets.choice(alphabet) for _ in range(10)))

    @classmethod
    def create_new(
        cls,
        name: str,
        description: str,
        price: int,
        cleaning_type: CleaningType,
    ) -> Cleaning:
        cleaning = cls(
            id=cls.next_id(),
            name=name,
            description=description,
            price=price,
            cleaning_type=cleaning_type.value if cleaning_type else None,
        )
        # add check rules here but later
        return cleaning
