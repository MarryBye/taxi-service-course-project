from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from src.controllers.auth import AuthController
from src.schemas.auth import AuthUserSchema, RegisterUserSchema
from src.schemas.token import TokenSchema, TokenDataSchema
from src.dependencies.get_current_user import get_current_user

router = APIRouter()

@router.post('/login')
async def login(
        req: Request,
        schema: AuthUserSchema,
        user: TokenDataSchema = Depends(get_current_user)
) -> TokenSchema:
    return AuthController.login(req, schema, user)

@router.post('/register')
async def register(
        req: Request,
        schema: RegisterUserSchema,
        user: TokenDataSchema = Depends(get_current_user)
) -> JSONResponse:
    return AuthController.register(req, schema, user)