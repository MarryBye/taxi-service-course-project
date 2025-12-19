from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.services.auth_service import AuthService
from src.schemas.auth import RegisterSchema, LoginSchema, TokenSchema, TokenDataSchema
from src.schemas.views import UsersView
from src.dependencies.require_auth import require_auth
from src.controllers.database import DatabaseController
from src.utils.crypto import CryptoUtil

router = APIRouter(prefix='/client')

@router.get('/profile')
def get_profile(user: TokenDataSchema = Depends(require_auth)):
    pass

@router.put('/profile')
def update_profile(user: TokenDataSchema = Depends(require_auth)):
    pass

@router.post('/orders')
def make_order(user: TokenDataSchema = Depends(require_auth)):
    pass

@router.get('/orders')
def orders_history(user: TokenDataSchema = Depends(require_auth)):
    pass

@router.get('/orders/{order_id}')
def order_info(order_id: int, user: TokenDataSchema = Depends(require_auth)):
    pass

@router.get('/orders/current')
def current_order(user: TokenDataSchema = Depends(require_auth)):
    pass

@router.post('/orders/current/cancel')
def cancel_order(user: TokenDataSchema = Depends(require_auth)):
    pass

@router.post('/orders/current/rate')
def rate_order(user: TokenDataSchema = Depends(require_auth)):
    pass

@router.get('/stats')
def stats(user: TokenDataSchema = Depends(require_auth)):
    pass