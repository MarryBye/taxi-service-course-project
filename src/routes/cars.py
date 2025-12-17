from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.cars import CarSchema, CreateCarSchema, UpdateCarSchema
from src.schemas.token import TokenDataSchema
from src.controllers.cars import CarsController
from src.dependencies.has_role import require_roles

router = APIRouter(prefix='/admin')

@router.get('/cars')
async def list(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> list[CarSchema]:
    return CarsController.list(req, current_user=current_user)

@router.get('/cars/{car_id}')
async def get(
        req: Request,
        car_id: int,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> CarSchema:
    return CarsController.detail(req, car_id=car_id, current_user=current_user)

@router.post('/cars')
async def create(
        req: Request,
        schema: CreateCarSchema,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return CarsController.create(req, schema=schema, current_user=current_user)

@router.put('/cars/{car_id}')
async def update(
        req: Request,
        car_id: int,
        schema: UpdateCarSchema,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return CarsController.update(req, car_id=car_id, schema=schema, current_user=current_user)

@router.delete('/cars/{car_id}')
async def delete(
        req: Request,
        car_id: int,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return CarsController.delete(req, car_id=car_id, current_user=current_user)

