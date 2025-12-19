from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.services.auth_service import AuthService
from src.schemas.auth import RegisterSchema, LoginSchema, TokenSchema, TokenDataSchema
from src.schemas.views import UsersView
from src.dependencies.require_auth import require_auth
from src.controllers.database import DatabaseController
from src.utils.crypto import CryptoUtil

router = APIRouter(prefix='/auth')

@router.post('/login')
async def login(data: LoginSchema) -> TokenSchema:
    result = AuthService.authenticate(data)

    if isinstance(result, Exception):
        raise HTTPException(400, str(result))

    if not result:
        raise HTTPException(401, "Invalid credentials")

    db = DatabaseController()
    db.connect(username=data.login, password=data.password)

    token_data = TokenDataSchema(
        id=result['id'],
        login=data.login,
        role=result['role']
    )

    token = CryptoUtil.create_access_token(token_data)

    return TokenSchema(
        access_token=token,
        token_type="bearer"
    )

@router.post('/register')
async def register(data: RegisterSchema) -> UsersView:
    result = AuthService.register(data)

    if isinstance(result, Exception):
        raise HTTPException(400, str(result))

    if not result:
        raise HTTPException(409, "User already exists")

    return result

@router.post('/logout')
async def logout(current_user: TokenDataSchema = Depends(require_auth)) -> JSONResponse:
    result = AuthService.logout(current_user)

    if isinstance(result, Exception):
        raise HTTPException(400, 'Error logging out')

    return JSONResponse(status_code=200, content={"detail": "Logged out successfully"})