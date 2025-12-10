from fastapi import APIRouter, Depends
from src.schemas.drivers import StaffSchema, StaffCreateSchema, StaffUpdateSchema
from src.schemas.token import TokenDataSchema
from src.controllers.staff import StaffController
from src.utils.auth import Auth

router = APIRouter()

@router.get('/staff')
async def list_staff(current_user: TokenDataSchema = Depends(Auth.verify_token)) -> list[StaffSchema]:
    return StaffController.list_view(current_user=current_user)

@router.get('/staff/{user_id}')
async def get_staff(user_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> StaffSchema:
    return StaffController.detail_view(user_id=user_id, current_user=current_user)

@router.post('/staff')
async def create_staff(schema: StaffCreateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> StaffSchema:
    return StaffController.create_view(schema=schema, current_user=current_user)

@router.put('/staff/{user_id}')
async def update_staff(user_id: int, schema: StaffUpdateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> StaffSchema:
    return StaffController.update_view(user_id=user_id, schema=schema, current_user=current_user)

@router.delete('/staff/{user_id}')
async def delete_staff(user_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> None:
    return StaffController.delete_view(user_id=user_id, current_user=current_user)