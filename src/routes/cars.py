from fastapi import APIRouter, Depends
from src.schemas.cars import CarSchema, CarCreateSchema, CarUpdateSchema
from src.schemas.token import TokenDataSchema
from src.controllers.cars import CarsController
from src.utils.auth import Auth

router = APIRouter()

@router.get('/cars')
async def list_cars(current_user: TokenDataSchema = Depends(Auth.verify_token)) -> list[CarSchema]:
    return CarsController.list_view(current_user=current_user)

@router.get('/cars/{car_id}')
async def get_car(car_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> CarSchema:
    return CarsController.detail_view(car_id=car_id, current_user=current_user)

@router.post('/cars')
async def create_car(schema: CarCreateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> CarSchema:
    return CarsController.create_view(schema=schema, current_user=current_user)

@router.put('/cars/{car_id}')
async def update_car(car_id: int, schema: CarUpdateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> CarSchema:
    return CarsController.update_view(car_id=car_id, schema=schema, current_user=current_user)

@router.delete('/cars/{car_id}')
async def delete_car(car_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> None:
    return CarsController.delete_view(car_id=car_id, current_user=current_user)