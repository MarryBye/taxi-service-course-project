from src.controllers.database import Database
from src.schemas.transactions import TransactionSchema, CreateTransactionSchema
from src.schemas.token import TokenDataSchema


class TransactionService:
    @staticmethod
    def get(id: int, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "SELECT * FROM admin.get_transaction(%s)"
        return db.execute(query, params=[id], fetch_count=1)

    @staticmethod
    def create(schema: CreateTransactionSchema, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.create_transaction(%s, %s, %s, %s, %s)"
        params = [
            schema.user_id,
            schema.balance_type,
            schema.transaction_type,
            schema.payment_method,
            schema.amount
        ]
        return db.execute(query, params=params, fetch_count=1)