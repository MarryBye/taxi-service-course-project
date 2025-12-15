from src.controllers.database import database
from src.schemas.auth import AuthUserSchema
from src.schemas.orders import CreateOrderSchema, RateOrderSchema, CancelOrderSchema


class OrdersService:
    @staticmethod
    def get_current(executor: AuthUserSchema):
        query = "SELECT * FROM authorized.get_current_order()"
        return database.execute(query, fetch_count=1, executor_data=executor)

    @staticmethod
    def history(executor: AuthUserSchema):
        query = "SELECT * FROM authorized.get_client_history()"
        return database.execute(query, fetch_count=-1, executor_data=executor)

    @staticmethod
    def make(schema: CreateOrderSchema, executor: AuthUserSchema):
        query = """
            CALL authorized.make_order(%s, %s, %s, %s)
        """
        params = [
            schema.order_class,
            schema.payment_method,
            schema.amount,
            schema.addresses
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)

    @staticmethod
    def cancel(schema: CancelOrderSchema, executor: AuthUserSchema):
        query = """
            CALL authorized.cancel_current_order(%s, %s)
        """
        params = [
            schema.comment,
            schema.driver_tags
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)

    @staticmethod
    def rate(schema: RateOrderSchema, executor: AuthUserSchema):
        query = """
            CALL authorized.rate_order_by_client(%s, %s, %s)
        """
        params = [
            schema.mark,
            schema.comment,
            schema.driver_tags
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)
