from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from src.services.admin.transaction_service import TransactionService
from src.schemas.transactions import TransactionSchema, CreateTransactionSchema
from src.schemas.token import TokenDataSchema


class TransactionsController:

    @staticmethod
    def detail(req: Request, transaction_id: int, current_user: TokenDataSchema) -> TransactionSchema:
        result = TransactionService.get(transaction_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        if not result:
            raise HTTPException(404, "Transaction not found")

        return result

    @staticmethod
    def create(req: Request, schema: CreateTransactionSchema, current_user: TokenDataSchema) -> JSONResponse:
        result = TransactionService.create(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(400, str(result))

        return JSONResponse({"detail": "Transaction created successfully"}, status_code=200)
