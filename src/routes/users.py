from fastapi import APIRouter, Depends
from src.schemas.users import UserCreateSchema, UserSchema, UserUpdateSchema
from src.schemas.token import TokenDataSchema
from src.controllers.users import UsersController
from src.utils.auth import Auth

router = APIRouter()

@router.get('/users')
async def list_users(current_user: TokenDataSchema = Depends(Auth.verify_token)) -> list[UserSchema]:
    return UsersController.list_view(current_user=current_user)

@router.get('/users/{user_id}')
async def get_user(user_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> UserSchema:
    return UsersController.detail_view(user_id=user_id, current_user=current_user)

@router.post('/users')
async def create_user(schema: UserCreateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> UserSchema:
    return UsersController.create_view(schema=schema, current_user=current_user)

@router.put('/users/{user_id}')
async def update_user(user_id: int, schema: UserUpdateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> UserSchema:
    return UsersController.update_view(user_id=user_id, schema=schema, current_user=current_user)

@router.delete('/users/{user_id}')
async def delete_user(user_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> None:
    return UsersController.delete_view(user_id=user_id, current_user=current_user)