from fastapi import APIRouter
from src.routes.api.cars import router as cars_router

router = APIRouter()

router.include_router(cars_router)