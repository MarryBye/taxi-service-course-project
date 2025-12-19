from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from src.schemas.transactions import TransactionSchema, CreateTransactionSchema
from src.schemas.token import TokenDataSchema
from src.controllers.transactions import TransactionsController
from src.dependencies.has_role import require_roles

router = APIRouter(prefix='/admin')

@router.get('/transactions/{transaction_id}')
async def get(
        req: Request,
        transaction_id: int,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> TransactionSchema:
    return TransactionsController.detail(req, transaction_id=transaction_id, current_user=current_user)

@router.post('/transactions')
async def create(
        req: Request,
        schema: CreateTransactionSchema,
        current_user: TokenDataSchema = Depends(require_roles('admin'))
) -> JSONResponse:
    return TransactionsController.create(req, schema=schema, current_user=current_user)