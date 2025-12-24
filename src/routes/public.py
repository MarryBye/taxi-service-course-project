from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.services.public import PublicService
from src.schemas.common import Country, City

router = APIRouter(prefix='/public')

@router.get('/countries')
async def get_countries() -> list[Country]:
    result = PublicService.get_countries()

    if isinstance(result, Exception):
        raise HTTPException(400, str(result))

    return result

@router.get('/countries/{country_id}/cities')
async def get_cities(country_id: int) -> list[City]:
    result = PublicService.get_cities(country_id)

    if isinstance(result, Exception):
        raise HTTPException(400, str(result))

    return result