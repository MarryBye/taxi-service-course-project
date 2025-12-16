from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from src.services.admin.orders_service import OrdersService
from src.schemas.orders import AdminCreateOrderSchema, AdminUpdateOrderSchema, OrderSchema
from src.schemas.token import TokenDataSchema


class OrdersController:

    @staticmethod
    def list(req: Request, current_user: TokenDataSchema) -> list[OrderSchema]:
        result = OrdersService.list(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "Orders not found")

        return result

    @staticmethod
    def detail(req: Request, order_id: int, current_user: TokenDataSchema) -> OrderSchema:
        result = OrdersService.get(order_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "Order not found")

        return result

    @staticmethod
    def create(req: Request, schema: AdminCreateOrderSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = OrdersService.create(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order created successfully"}, status_code=200)

    @staticmethod
    def update(
        req: Request,
        order_id: int,
        schema: AdminUpdateOrderSchema,
        current_user: TokenDataSchema
    ) -> JSONResponse:
        result = OrdersService.update(order_id, schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order updated successfully"}, status_code=200)

    @staticmethod
    def delete(req: Request, order_id: int, current_user: TokenDataSchema) -> JSONResponse:
        result = OrdersService.delete(order_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order deleted successfully"}, status_code=200)
