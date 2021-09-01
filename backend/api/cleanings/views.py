from typing import List

from api import urls
from api.deps import App
from domain.cleanings.selectors import CleaningDataDto
from domain.cleanings.services import CreateCleaningDto, UpdateCleaningDto
from fastapi import APIRouter, Depends, Path, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from domain.types import CleaningID

router = APIRouter()


class CreateCleaningInputSchema(CreateCleaningDto):
    ...


class CleaningDataOutputSchema(CleaningDataDto):
    ...


class UpdateCleaningSchema(UpdateCleaningDto):
    ...


@router.post(
    urls.Cleanings.create_cleaning_url,
    name=urls.Cleanings.create_cleaning_name,
    response_model=CleaningDataOutputSchema,
    status_code=HTTP_201_CREATED,
)
def create_new_cleaning(
    data: CreateCleaningInputSchema, app: App = Depends()
) -> CleaningDataDto:
    dto = CreateCleaningDto(**data.dict())
    cleaning_id = app.container.cleaning_service.create_cleaning(dto)

    return app.container.cleaning_selector.get_cleaning_data(cleaning_id=cleaning_id)


@router.get(
    urls.Cleanings.get_cleaning_url,
    name=urls.Cleanings.get_cleaning_name,
    response_model=CleaningDataOutputSchema,
    status_code=HTTP_200_OK
)
def get_cleaning_by_id(
        # cleaning_id: str = Path(...),
        cleaning_id: CleaningID,
        app: App = Depends()
) -> CleaningDataDto:
    cleaning = app.container.cleaning_selector.get_cleaning_data(cleaning_id=cleaning_id)
    if not cleaning:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No cleaning found with that id")
    return cleaning


@router.get(
    urls.Cleanings.get_all_cleanings_url,
    name=urls.Cleanings.get_all_cleaning_name,
    response_model=List[CleaningDataOutputSchema],
)
def get_all_cleanings(
        app: App = Depends()
) -> List[CleaningDataDto]:
    cleanings = app.container.cleaning_selector.get_all_cleanings()
    return cleanings


@router.patch(
    urls.Cleanings.update_cleaning_url,
    name=urls.Cleanings.update_cleaning_name,
    response_model=CleaningDataOutputSchema
)
def update_cleaning_by_id(
        cleaning_id: CleaningID,
        data: CreateCleaningInputSchema,
        app: App = Depends(),
) -> CleaningDataDto:
    dto = UpdateCleaningDto(**data.dict())
    updated_cleaning = app.container.cleaning_service.update_cleaning(cleaning_id=cleaning_id, dto=dto)
    return updated_cleaning















