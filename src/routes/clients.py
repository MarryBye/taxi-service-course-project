from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.clients import ClientSchema, CancelOrderSchema, MakeOrderSchema, RateOrderSchema, UpdateProfileSchema
from src.schemas.orders import OrderSchema
from src.schemas.token import TokenDataSchema
from src.controllers.clients import ClientsController
from src.utils.auth import Auth

router = APIRouter(prefix='/authorized')

@router.post('/cancel_order')
async def cancel_order(
        req: Request,
        schema: CancelOrderSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return ClientsController.cancel_order(req, schema=schema, current_user=current_user)

@router.post('/make_order')
async def make_order(
        req: Request,
        schema: MakeOrderSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return ClientsController.make_order(req, schema=schema, current_user=current_user)

@router.post('/rate_order')
async def rate_order(
        req: Request,
        schema: RateOrderSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return ClientsController.rate_order(req, schema=schema, current_user=current_user)

@router.put('/update_profile')
async def update_profile(
        req: Request,
        schema: UpdateProfileSchema,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> JSONResponse:
    return ClientsController.update_profile(req, schema=schema, current_user=current_user)

@router.get('/get_history')
async def get_history(
        req: Request,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> list[OrderSchema]:
    return ClientsController.get_history(req, current_user=current_user)

@router.get('/current_order')
async def current_order(
        req: Request,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> OrderSchema:
    return ClientsController.current_order(req, current_user=current_user)

@router.get('/profile')
async def profile(
        req: Request,
        current_user: TokenDataSchema = Depends(Auth.verify_user)
) -> ClientSchema:
    return ClientsController.profile(req, current_user=current_user)