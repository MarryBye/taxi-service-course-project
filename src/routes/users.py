from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.users import CreateUserSchema, UpdateUserSchema, UserSchema
from src.schemas.auth import AuthUserSchema
from src.schemas.token import TokenDataSchema
from src.controllers.users import UsersController
from src.utils.auth import Auth

router = APIRouter(prefix='/admin')

@router.get('/users')
async def list_users(
        req: Request,
        current_user: AuthUserSchema = Depends(Auth.verify_user)
) -> list[UserSchema]:
    return UsersController.list_view(req, current_user=current_user)

@router.get('/users/{user_id}')
async def get_user(
        req: Request,
        user_id: int,
        current_user: AuthUserSchema = Depends(Auth.verify_user)
) -> UserSchema:
    return UsersController.detail_view(req, user_id=user_id, current_user=current_user)

@router.post('/users')
async def create_user(
        req: Request,
        schema: CreateUserSchema,
        current_user: AuthUserSchema = Depends(Auth.verify_user)
) -> UserSchema:
    return UsersController.create_view(req, schema=schema, current_user=current_user)

@router.put('/users/{user_id}')
async def update_user(
        req: Request,
        user_id: int,
        schema: UpdateUserSchema,
        current_user: AuthUserSchema = Depends(Auth.verify_user)
) -> UserSchema:
    return UsersController.update_view(req, user_id=user_id, schema=schema, current_user=current_user)

@router.delete('/users/{user_id}')
async def delete_user(
        req: Request,
        user_id: int,
        current_user: AuthUserSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return UsersController.delete_view(req, user_id=user_id, current_user=current_user)

