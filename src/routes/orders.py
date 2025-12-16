from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.orders import OrderSchema, AdminCreateOrderSchema, AdminUpdateOrderSchema
from src.schemas.token import TokenDataSchema
from src.controllers.orders import OrdersController
from src.utils.auth import Auth

router = APIRouter(prefix='/admin')

@router.get('/orders')
async def list(
        req: Request,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> list[OrderSchema]:
    return OrdersController.list(req, current_user=current_user)

@router.get('/orders/{order_id}')
async def get(
        req: Request,
        order_id: int,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> OrderSchema:
    return OrdersController.detail(req, order_id=order_id, current_user=current_user)

@router.post('/orders')
async def create(
        req: Request,
        schema: AdminCreateOrderSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return OrdersController.create(req, schema=schema, current_user=current_user)

@router.put('/orders/{order_id}')
async def update(
        req: Request,
        order_id: int,
        schema: AdminUpdateOrderSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return OrdersController.update(req, order_id=order_id, schema=schema, current_user=current_user)

@router.delete('/orders/{order_id}')
async def delete(
        req: Request,
        order_id: int,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return OrdersController.delete(req, order_id=order_id, current_user=current_user)

