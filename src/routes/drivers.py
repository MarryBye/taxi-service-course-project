from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.drivers import DriverSchema, AcceptOrderSchema, CancelOrderSchema, RateOrderSchema
from src.schemas.orders import OrderSchema
from src.schemas.token import TokenDataSchema
from src.controllers.workers import WorkersController
from src.dependencies.has_role import require_roles

router = APIRouter(prefix='/workers')

@router.post('/cancel_order')
async def cancel_order(
        req: Request,
        schema: CancelOrderSchema,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> JSONResponse:
    return WorkersController.cancel_order(req, schema=schema, current_user=current_user)

@router.post('/accept_order')
async def accept_order(
        req: Request,
        schema: AcceptOrderSchema,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> JSONResponse:
    return WorkersController.accept_order(req, schema=schema, current_user=current_user)

@router.post('/complete_order')
async def complete_order(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> JSONResponse:
    return WorkersController.complete_order(req, current_user=current_user)

@router.post('/rate_order')
async def rate_order(
        req: Request,
        schema: RateOrderSchema,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> JSONResponse:
    return WorkersController.rate_order(req, schema=schema, current_user=current_user)

@router.post('/submit_arrive')
async def submit_arrive(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> JSONResponse:
    return WorkersController.submit_arrive(req, current_user=current_user)

@router.get('/acceptable_orders')
async def acceptable_orders(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> list[OrderSchema]:
    return WorkersController.acceptable_orders(req, current_user=current_user)

@router.get('/current_order')
async def current_order(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> OrderSchema:
    return WorkersController.current_order(req, current_user=current_user)

@router.get('/history')
async def history(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> list[OrderSchema]:
    return WorkersController.history(req, current_user=current_user)

@router.get('/stats')
async def stats(
        req: Request,
        current_user: TokenDataSchema = Depends(require_roles('driver'))
) -> DriverSchema:
    return WorkersController.stats(req, current_user=current_user)