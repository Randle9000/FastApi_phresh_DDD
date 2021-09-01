from pydantic import BaseModel, Extra


class BasePydanticModel(BaseModel):
    class Config:
        orm_mode = True  # Pydantic models can be created from arbitrary class instances to support models that map to ORM objects.
        allow_mutation = False  # immutable
        extra = Extra.forbid  #
        validate_assignment = True  # whether to perform validation on assignment to attributes


    def __hash__(self) -> int:
        return hash((type(self),) + tuple(self.__dict__.values()))


class BaseDto(BasePydanticModel):
    ...
