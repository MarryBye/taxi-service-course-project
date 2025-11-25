from fastapi import APIRouter
from src.routes.api.index import router as api_router

router = APIRouter()

router.include_router(api_router, prefix="/api", tags=["api"])