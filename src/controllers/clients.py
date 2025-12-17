from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Any
from src.services.client_service import ClientService
from src.schemas.clients import (
    CancelOrderSchema,
    MakeOrderSchema,
    RateOrderSchema,
    UpdateProfileSchema,
    ClientSchema
)
from src.schemas.orders import OrderSchema
from src.schemas.token import TokenDataSchema


class ClientsController:

    @staticmethod
    def cancel_order(req: Request, schema: CancelOrderSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = ClientService.cancel_current_order(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order canceled"}, status_code=200)

    @staticmethod
    def make_order(req: Request, schema: MakeOrderSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = ClientService.make_order(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order created"}, status_code=200)

    @staticmethod
    def rate_order(req: Request, schema: RateOrderSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = ClientService.rate_order_by_client(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Order rated"}, status_code=200)

    @staticmethod
    def update_profile(req: Request, schema: UpdateProfileSchema, current_user: TokenDataSchema) -> JSONResponse:
        schema.hash_password()
        result = ClientService.update_profile(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Profile updated"}, status_code=200)

    @staticmethod
    def get_history(req: Request, current_user: TokenDataSchema) -> list[OrderSchema]:
        result = ClientService.get_client_history(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return result

    @staticmethod
    def current_order(req: Request, current_user: TokenDataSchema) -> OrderSchema:
        result = ClientService.get_current_order(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "No active order")

        return result

    @staticmethod
    def profile(req: Request, current_user: TokenDataSchema) -> ClientSchema | None:
        result = ClientService.get_profile(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "Profile not found")

        return result
