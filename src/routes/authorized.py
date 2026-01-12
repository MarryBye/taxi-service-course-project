from fastapi import APIRouter, Depends, HTTPException
from src.schemas.auth import TokenDataSchema
from src.dependencies.require_auth import require_auth
from src.schemas.views import *
from src.schemas.authorized import *
from src.services.authorized import AuthorizedService

router = APIRouter(prefix='/client')

@router.get('/profile')
async def get_profile(user: TokenDataSchema = Depends(require_auth)) -> UsersView:
    data = AuthorizedService.get_profile(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.put('/profile')
async def update_profile(data: UpdateProfile, user: TokenDataSchema = Depends(require_auth)) -> UsersView:
    data = AuthorizedService.update_profile(data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders')
async def make_order(data: MakeOrderSchema, user: TokenDataSchema = Depends(require_auth)) -> OrdersView:
    data = AuthorizedService.make_order(data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders')
async def orders_history(user: TokenDataSchema = Depends(require_auth)) -> list[OrdersView]:
    data = AuthorizedService.orders_history(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders/current')
async def current_order(user: TokenDataSchema = Depends(require_auth)) -> OrdersView | None:
    data = AuthorizedService.current_order(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders/{order_id}')
async def order_info(order_id: int, user: TokenDataSchema = Depends(require_auth)) -> OrdersView:
    data = AuthorizedService.get_order(order_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders/{order_id}/stat')
async def order_stat(order_id: int, user: TokenDataSchema = Depends(require_auth)) -> OrdersStatView:
    data = AuthorizedService.order_stat(order_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders/{order_id}/cancel')
async def cancel_order(order_id: int, data: CancelOrderSchema, user: TokenDataSchema = Depends(require_auth)) -> OrdersStatView:
    data = AuthorizedService.cancel_order(order_id, data, user)
    print(data)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders/{order_id}/rate')
async def rate_order(order_id: int, data: RateOrderSchema, user: TokenDataSchema = Depends(require_auth)) -> OrdersStatView:
    data = AuthorizedService.rate_order(order_id, data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/stats')
async def stats(user: TokenDataSchema = Depends(require_auth)) -> ClientsStatView:
    data = AuthorizedService.stats(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.put('/add_funds')
async def add_funds(data: AddFundsSchema, user: TokenDataSchema = Depends(require_auth)) -> None:
    data = AuthorizedService.add_funds(data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data