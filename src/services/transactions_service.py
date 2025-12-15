from src.controllers.database import database
from src.schemas.auth import AuthUserSchema
from src.schemas.transactions import CreateTransactionSchema


class TransactionsService:
    @staticmethod
    def get(id: int, executor: AuthUserSchema = None):
        query = "SELECT * FROM admin.get_transaction(%s)"
        return database.execute(query, params=[id], fetch_count=1, executor_data=executor)

    @staticmethod
    def create(schema: CreateTransactionSchema, executor: AuthUserSchema = None):
        query = """
            CALL admin.create_transaction(%s, %s, %s, %s, %s)
        """
        params = [
            schema.user_id,
            schema.balance_type,
            schema.transaction_type,
            schema.payment_method,
            schema.amount
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)
