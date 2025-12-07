from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.services.orders_service import OrdersService
from src.schemas.orders import OrderSchema, OrderCreateSchema, OrderUpdateSchema
from src.schemas.token import TokenDataSchema

class OrdersController:
    @staticmethod
    def list_view(current_user: TokenDataSchema, client_id: int | None = None, driver_id: int | None = None) -> list[OrderSchema]:
        if client_id is not None:
            orders = OrdersService.get_client_orders(client_id=client_id)
        elif driver_id is not None:
            orders = OrdersService.get_driver_orders(driver_id=driver_id)
        else:
            orders = OrdersService.list()
        return orders
    
    @staticmethod
    def detail_view(order_id: int, current_user: TokenDataSchema) -> OrderSchema:
        order = OrdersService.get(order_id)
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
        return order

    @staticmethod
    def create_view(schema: OrderCreateSchema, current_user: TokenDataSchema) -> OrderSchema:
        order = OrdersService.create(
            client_id=schema.client_id
        )
        return order

    @staticmethod
    def update_view(order_id: int, schema: OrderUpdateSchema, current_user: TokenDataSchema) -> OrderSchema:
        order = OrdersService.update(
            id=order_id,
            driver_id=schema.driver_id,
            status=schema.status,
            finished_at=schema.finished_at
        )
        return order

    @staticmethod
    def delete_view(order_id: int, current_user: TokenDataSchema) -> None:
        OrdersService.delete(order_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Order deleted successfully"})