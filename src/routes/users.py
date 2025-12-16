from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.users import AdminCreateUserSchema, AdminUpdateUserSchema, UserSchema
from src.schemas.token import TokenDataSchema
from src.controllers.users import UsersController
from src.utils.auth import Auth

router = APIRouter(prefix='/admin')

@router.get('/users')
async def list_users(
        req: Request,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> list[UserSchema]:
    return UsersController.list(req, current_user=current_user)

@router.get('/users/{user_id}')
async def get_user(
        req: Request,
        user_id: int,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> UserSchema:
    return UsersController.detail(req, user_id=user_id, current_user=current_user)

@router.post('/users')
async def create_user(
        req: Request,
        schema: AdminCreateUserSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return UsersController.create(req, schema=schema, current_user=current_user)

@router.put('/users/{user_id}')
async def update_user(
        req: Request,
        user_id: int,
        schema: AdminUpdateUserSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return UsersController.update(req, user_id=user_id, schema=schema, current_user=current_user)

@router.delete('/users/{user_id}')
async def delete_user(
        req: Request,
        user_id: int,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return UsersController.delete(req, user_id=user_id, current_user=current_user)

