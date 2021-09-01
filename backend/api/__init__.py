from api.cleanings.views import router as cleanings_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(cleanings_router, prefix="/cleanings", tags=["cleanings"])
