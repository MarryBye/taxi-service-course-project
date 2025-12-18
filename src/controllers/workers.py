from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from src.services.worker_service import WorkersService
from src.schemas.drivers import AcceptOrderSchema, CancelOrderSchema, RateOrderSchema, DriverSchema
from src.schemas.orders import OrderSchema
from src.schemas.token import TokenDataSchema


class WorkersController:

    @staticmethod
    def acceptable_orders(req: Request, current_user: TokenDataSchema) -> list[OrderSchema]:
        print(current_user)
        result = WorkersService.get_acceptable_orders(user=current_user)
        print(result)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return result

    @staticmethod
    def accept_order(req: Request, schema: AcceptOrderSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = WorkersService.accept_order(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order accepted"}, status_code=200)

    @staticmethod
    def cancel_order(req: Request, schema: CancelOrderSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = WorkersService.cancel_order(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order canceled"}, status_code=200)

    @staticmethod
    def submit_arrive(req: Request, current_user: TokenDataSchema) -> JSONResponse:
        result = WorkersService.submit_arriving_time(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Arrival submitted"}, status_code=200)

    @staticmethod
    def submit_start(req: Request, current_user: TokenDataSchema) -> JSONResponse:
        result = WorkersService.submit_start_ride(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Ride started"}, status_code=200)

    @staticmethod
    def complete_order(req: Request, current_user: TokenDataSchema) -> JSONResponse:
        result = WorkersService.complete_order(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order completed"}, status_code=200)

    @staticmethod
    def current_order(req: Request, current_user: TokenDataSchema) -> OrderSchema:
        result = WorkersService.get_current_order(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "No active order")

        return result

    @staticmethod
    def history(req: Request, current_user: TokenDataSchema) -> list[OrderSchema]:
        result = WorkersService.get_driver_history(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return result

    @staticmethod
    def stats(req: Request, current_user: TokenDataSchema) -> DriverSchema:
        result = WorkersService.get_own_stats(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return result

    @staticmethod
    def rate_order(
        req: Request,
        schema: RateOrderSchema,
        current_user: TokenDataSchema
    ) -> JSONResponse:
        result = WorkersService.rate_order_by_driver(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(result)
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"detail": "Order rated successfully"}
        )