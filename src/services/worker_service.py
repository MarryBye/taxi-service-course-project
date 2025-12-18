from src.controllers.database import Database
from src.schemas.drivers import AcceptOrderSchema, CancelOrderSchema, RateOrderSchema
from src.schemas.token import TokenDataSchema


class WorkersService:
    @staticmethod
    def accept_order(schema: AcceptOrderSchema, user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL workers.accept_order(%s, %s)"
        params = [
            user.id,
            schema.order_id
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def cancel_order(schema: CancelOrderSchema, user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL workers.cancel_order(%s, %s, %s::public.client_cancel_tags[])"
        params = [
            user.id,
            schema.comment,
            [
                tag for tag in schema.client_tags
            ]
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def submit_arriving_time(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL workers.submit_arriving_time(%s)"
        params = [
            user.id
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def submit_start_ride(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL workers.submit_start_ride(%s)"
        params = [
            user.id
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def complete_order(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL workers.complete_order(%s)"
        params = [
            user.id
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def get_acceptable_orders(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "SELECT * FROM workers.get_acceptable_orders(%s)"
        params = [
            user.id
        ]

        return db.execute(query, params=params, fetch_count=-1)

    @staticmethod
    def get_current_order(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "SELECT * FROM workers.get_current_order(%s)"
        params = [
            user.id
        ]

        return db.execute(query, params=params, fetch_count=1)

    @staticmethod
    def get_driver_history(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "SELECT * FROM workers.get_driver_history(%s)"
        params = [
            user.id
        ]

        return db.execute(query, params=params, fetch_count=-1)

    @staticmethod
    def rate_order_by_driver(schema: RateOrderSchema, user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL workers.rate_order_by_driver(%s, %s, %s, %s::public.client_tags[])"
        params = [
            user.id,
            schema.mark,
            schema.comment,
            [
                tag for tag in schema.client_tags
            ]
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def get_own_stats(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "SELECT * FROM workers.get_own_stats(%s)"
        params = [
            user.id
        ]

        return db.execute(query, params=params, fetch_count=1)