from src.controllers.database import database
from src.schemas.auth import AuthUserSchema
from src.schemas.orders import RateOrderSchema, CancelOrderSchema


class WorkersService:
    @staticmethod
    def get_current_order(executor: AuthUserSchema):
        query = "SELECT * FROM workers.get_current_order()"
        return database.execute(query, fetch_count=1, executor_data=executor)

    @staticmethod
    def acceptable_orders(executor: AuthUserSchema):
        query = "SELECT * FROM workers.get_acceptable_orders()"
        return database.execute(query, fetch_count=-1, executor_data=executor)

    @staticmethod
    def accept(order_id: int, executor: AuthUserSchema):
        query = "CALL workers.accept_order(%s)"
        return database.execute(query, params=[order_id], fetch_count=0, executor_data=executor)

    @staticmethod
    def arrive(executor: AuthUserSchema):
        query = "CALL workers.submit_arriving_time()"
        return database.execute(query, fetch_count=0, executor_data=executor)

    @staticmethod
    def complete(executor: AuthUserSchema):
        query = "CALL workers.complete_order()"
        return database.execute(query, fetch_count=0, executor_data=executor)

    @staticmethod
    def cancel(schema: CancelOrderSchema, executor: AuthUserSchema):
        query = "CALL workers.cancel_order(%s, %s)"
        params = [
            schema.comment,
            schema.client_tags
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)

    @staticmethod
    def rate(schema: RateOrderSchema, executor: AuthUserSchema):
        query = "CALL workers.rate_order_by_driver(%s, %s, %s)"
        params = [
            schema.mark,
            schema.comment,
            schema.client_tags
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)

    @staticmethod
    def history(executor: AuthUserSchema):
        query = "SELECT * FROM workers.get_driver_history()"
        return database.execute(query, fetch_count=-1, executor_data=executor)

    @staticmethod
    def stats(executor: AuthUserSchema):
        query = "SELECT * FROM workers.get_own_stats()"
        return database.execute(query, fetch_count=1, executor_data=executor)
