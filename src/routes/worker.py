from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.services.auth_service import AuthService
from src.schemas.auth import RegisterSchema, LoginSchema, TokenSchema, TokenDataSchema
from src.schemas.views import UsersView
from src.dependencies.has_role import require_roles
from src.controllers.database import DatabaseController
from src.utils.crypto import CryptoUtil

router = APIRouter(prefix='/driver')

@router.get('/orders')
def orders_history(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.get('/orders/acceptable')
def acceptable_orders(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.post('/orders/new/accept')
def accept_order(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.post('/orders/current/cancel')
def cancel_order(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.get('/orders/current')
def current_order(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.post('/orders/current/rate')
def rate_order(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.post('/orders/current/arrive')
def submit_arrival(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.post('/orders/current/start')
def submit_start(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.post('/orders/current/finish')
def submit_finish(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass

@router.get('/stats')
def stats(user: TokenDataSchema = Depends(require_roles('driver'))):
    pass