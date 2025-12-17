from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.users import AdminCreateUserSchema, AdminUpdateUserSchema, UserSchema
from src.schemas.token import TokenDataSchema
from src.controllers.users import UsersController
from src.dependencies.has_role import require_roles

router = APIRouter(prefix='/admin')

@router.get('/users')
async def list(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> list[UserSchema]:
    return UsersController.list(req, current_user=current_user)

@router.get('/users/{user_id}')
async def get(
        req: Request,
        user_id: int,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> UserSchema:
    return UsersController.detail(req, user_id=user_id, current_user=current_user)

@router.post('/users')
async def create(
        req: Request,
        schema: AdminCreateUserSchema,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return UsersController.create(req, schema=schema, current_user=current_user)

@router.put('/users/{user_id}')
async def update(
        req: Request,
        user_id: int,
        schema: AdminUpdateUserSchema,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return UsersController.update(req, user_id=user_id, schema=schema, current_user=current_user)

@router.delete('/users/{user_id}')
async def delete(
        req: Request,
        user_id: int,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return UsersController.delete(req, user_id=user_id, current_user=current_user)

