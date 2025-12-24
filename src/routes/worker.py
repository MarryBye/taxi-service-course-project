from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.schemas.auth import TokenDataSchema
from src.schemas.views import *
from src.schemas.workers import *

from src.dependencies.has_role import require_roles

from src.services.worker import WorkersService

router = APIRouter(prefix='/driver')

@router.get('/orders')
async def orders_history(user: TokenDataSchema = Depends(require_roles('driver'))) -> list[OrdersView]:
    data = WorkersService.orders_history(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders/current')
async def current_order(user: TokenDataSchema = Depends(require_roles('driver'))) -> OrdersView | None:
    data = WorkersService.current_order(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders/acceptable')
async def acceptable_orders(user: TokenDataSchema = Depends(require_roles('driver'))) -> list[OrdersView]:
    data = WorkersService.acceptable_orders(user)
    print(data)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/orders/{order_id}')
async def order_stat(order_id: int, user: TokenDataSchema = Depends(require_roles('driver'))) -> OrdersStatView:
    data = WorkersService.order_stat(order_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders/{order_id}/accept')
async def accept_order(order_id: int, user: TokenDataSchema = Depends(require_roles('driver'))) -> OrdersView:
    data = WorkersService.accept_order(order_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders/{order_id}/rate')
async def rate_order(order_id: int, data: RateOrderSchema, user: TokenDataSchema = Depends(require_roles('driver'))) -> OrdersStatView:
    data = WorkersService.rate_order(order_id, data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders/{order_id}/cancel')
async def cancel_order(order_id: int, data: CancelOrderSchema, user: TokenDataSchema = Depends(require_roles('driver'))) -> OrdersStatView:
    data = WorkersService.cancel_order(order_id, data, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders/{order_id}/arrive')
async def submit_arrival(order_id: int, user: TokenDataSchema = Depends(require_roles('driver'))) -> OrdersView:
    data = WorkersService.submit_arrival(order_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders/{order_id}/start')
async def submit_start(order_id: int, user: TokenDataSchema = Depends(require_roles('driver'))) -> OrdersView:
    data = WorkersService.submit_start(order_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.post('/orders/{order_id}/finish')
async def submit_finish(order_id: int, user: TokenDataSchema = Depends(require_roles('driver'))) -> OrdersView:
    data = WorkersService.submit_start(order_id, user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data

@router.get('/stats')
async def stats(user: TokenDataSchema = Depends(require_roles('driver'))) -> DriversStatView:
    data = WorkersService.stats(user)

    if isinstance(data, Exception):
        raise HTTPException(400, str(data))

    return data