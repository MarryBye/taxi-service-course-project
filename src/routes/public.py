from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.public import CurrentUserSchema
from src.schemas.token import TokenDataSchema
from src.controllers.public import PublicController
from src.utils.auth import Auth

router = APIRouter(prefix='/public')

@router.get('/me')
async def me(
        req: Request,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> CurrentUserSchema:
    return PublicController.current_user(req, current_user=current_user)