from fastapi import APIRouter, Depends
from src.schemas.drivers import DriverSchema, DriverCreateSchema, DriverUpdateSchema
from src.schemas.token import TokenDataSchema
from src.controllers.drivers import DriversController
from src.utils.auth import Auth

router = APIRouter()

@router.get('/drivers')
async def list_drivers(current_user: TokenDataSchema = Depends(Auth.verify_token)) -> list[DriverSchema]:
    return DriversController.list_view(current_user=current_user)

@router.get('/drivers/{user_id}')
async def get_driver(user_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> DriverSchema:
    return DriversController.detail_view(user_id=user_id, current_user=current_user)

@router.post('/drivers')
async def create_driver(schema: DriverCreateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> DriverSchema:
    return DriversController.create_view(schema=schema, current_user=current_user)

@router.put('/drivers/{user_id}')
async def update_driver(user_id: int, schema: DriverUpdateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> DriverSchema:
    return DriversController.update_view(user_id=user_id, schema=schema, current_user=current_user)

@router.delete('/drivers/{user_id}')
async def delete_driver(user_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> None:
    return DriversController.delete_view(user_id=user_id, current_user=current_user)