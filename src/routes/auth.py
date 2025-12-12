from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from src.controllers.auth import AuthController
from src.schemas.auth import AuthUserSchema, RegisterUserSchema
from src.schemas.token import TokenSchema, TokenDataSchema
from src.utils.auth import Auth

router = APIRouter()

@router.post('/login')
async def login(
        req: Request,
        schema: AuthUserSchema,
        user: TokenDataSchema = Depends(Auth.verify_user)
) -> TokenSchema:
    return AuthController.login(req, schema, user)

@router.post('/register')
async def register(
        req: Request,
        schema: RegisterUserSchema,
        user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return AuthController.register(req, schema, user)

@router.get('/logout')
async def logout(
        req: Request,
        user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return AuthController.logout(req, user)