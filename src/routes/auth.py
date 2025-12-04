from fastapi import APIRouter, Depends
from src.schemas.users import UserSchema, UserRegisterSchema, UserLoginSchema
from src.schemas.token import TokenSchema
from src.controllers.auth import AuthController
from src.utils.auth import Auth

router = APIRouter()

@router.post('/login')
async def login(schema: UserLoginSchema) -> TokenSchema:
    return AuthController.login(schema)

@router.post('/register')
async def register(schema: UserRegisterSchema) -> UserSchema:
    return AuthController.register(schema)
    