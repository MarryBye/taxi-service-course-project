from fastapi import APIRouter, Depends
from src.schemas.orders import OrderSchema, OrderCreateSchema, OrderUpdateSchema
from src.schemas.token import TokenDataSchema
from src.controllers.orders import OrdersController
from src.utils.auth import Auth

router = APIRouter()

@router.get('/orders')
async def list_orders(current_user: TokenDataSchema = Depends(Auth.verify_token), client_id: int | None = None, driver_id: int | None = None) -> list[OrderSchema]:
    return OrdersController.list_view(current_user=current_user, client_id=client_id, driver_id=driver_id)

@router.get('/orders/{order_id}')
async def get_order(order_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> OrderSchema:
    return OrdersController.detail_view(order_id=order_id, current_user=current_user)

@router.post('/orders')
async def create_order(schema: OrderCreateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> OrderSchema:
    return OrdersController.create_view(schema=schema, current_user=current_user)

@router.put('/orders/{order_id}')
async def update_order(order_id: int, schema: OrderUpdateSchema, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> OrderSchema:
    return OrdersController.update_view(order_id=order_id, schema=schema, current_user=current_user)

@router.delete('/orders/{order_id}')
async def delete_order(order_id: int, current_user: TokenDataSchema = Depends(Auth.verify_token)) -> None:
    return OrdersController.delete_view(order_id=order_id, current_user=current_user)