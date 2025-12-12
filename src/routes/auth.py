from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from src.controllers.auth import AuthController
from src.schemas.auth import AuthUserSchema, RegisterUserSchema
from src.schemas.token import TokenSchema
from src.utils.auth import Auth

router = APIRouter()

@router.post('/login')
async def login(
        req: Request,
        schema: AuthUserSchema,
        current_user: AuthUserSchema = Depends(Auth.verify_user)
) -> TokenSchema:
    return AuthController.login(req, schema, current_user)

@router.post('/register')
async def register(
        req: Request,
        schema: RegisterUserSchema,
        current_user: AuthUserSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return AuthController.register(req, schema, current_user)

@router.get('/logout')
async def logout(
        req: Request,
        current_user: AuthUserSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return AuthController.logout(req, current_user)