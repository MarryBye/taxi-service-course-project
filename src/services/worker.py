from src.controllers.database import DatabaseController
from src.schemas.auth import TokenDataSchema
from src.schemas.views import *
from src.schemas.workers import *


class WorkersService:
    @staticmethod
    def accept_order(order_id: int, user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """
            SELECT * FROM workers.accept_order(%s)
        """
        params = [order_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def acceptable_orders(user: TokenDataSchema = None) -> Exception | list[OrdersView]:
        db = DatabaseController()

        query = """SELECT * FROM workers.acceptable_orders()"""
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def cancel_order(order_id: int, data: CancelOrderSchema, user: TokenDataSchema = None) -> Exception | OrdersStatView:
        db = DatabaseController()

        query = """
                SELECT * FROM workers.cancel_order(
                    p_order_id := %s, 
                    p_comment := %s, 
                    p_tags := %s::VARCHAR(32)[]
                )
        """
        params = [
            order_id,
            data.comment,
            [
                tag for tag in data.tags
            ]
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def current_order(user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """
            SELECT * FROM workers.current_order()
        """
        params = []

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def order_stat(order_id: int, user: TokenDataSchema = None) -> Exception | OrdersStatView:
        db = DatabaseController()

        query = """
            SELECT * FROM workers.order_stat(%s)
        """
        params = [order_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def orders_history(user: TokenDataSchema = None) -> Exception | list[OrdersView]:
        db = DatabaseController()

        query = """SELECT * FROM workers.orders_history()"""
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def rate_order(order_id: int, data: RateOrderSchema, user: TokenDataSchema = None) -> Exception | OrdersStatView:
        db = DatabaseController()

        query = """
            SELECT * FROM workers.rate_order(
                    p_order_id := %s, 
                    p_mark := %s, 
                    p_comment := %s, 
                    p_tags := %s::VARCHAR(32)[]
            )
        """
        params = [
            order_id,
            data.mark,
            data.comment,
            [
                tag for tag in data.tags
            ]
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def stats(user: TokenDataSchema = None) -> Exception | DriversStatView:
        db = DatabaseController()

        query = """
            SELECT * FROM workers.stats()
        """
        params = []

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def submit_arrival(order_id: int, user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """
            SELECT * FROM workers.submit_arrival()
        """
        params = []

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def submit_finish(order_id: int, user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """
            SELECT * FROM workers.submit_finish()
        """
        params = []

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def submit_start(order_id: int, user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """
            SELECT * FROM workers.submit_start()
        """
        params = []

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)