from src.controllers.database import DatabaseController
from src.schemas.auth import TokenDataSchema
from src.schemas.views import *
from src.schemas.authorized import *


class AuthorizedService:
    @staticmethod
    def stats(user: TokenDataSchema = None) -> Exception | ClientsStatView:
        db = DatabaseController()

        query = """
            SELECT * FROM authorized.stats()
        """
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def get_profile(user: TokenDataSchema = None) -> Exception | UsersView:
        db = DatabaseController()

        query = """
            SELECT * FROM authorized.get_profile()
        """
        params = []

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def current_order(user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """
            SELECT * FROM authorized.current_order()
        """
        params = []

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def cancel_order(order_id: int, data: CancelOrderSchema, user: TokenDataSchema = None) -> Exception | OrdersStatView:
        db = DatabaseController()

        query = """
            SELECT * FROM authorized.cancel_order(
                p_order_id := %s, 
                p_comment := %s, 
                p_tags := %s::public.driver_cancel_tags[]
            )
        """
        params = [
            order_id,
            data.comment,
            [
                tag for tag in data.tags
            ]
        ]

        return db.execute(query, params=params, fetch_count=0, executor_username=user.login)

    @staticmethod
    def make_order(data: MakeOrderSchema, user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """
            SELECT * FROM authorized.make_order(
                p_order_class := %s, 
                p_payment_method := %s, 
                p_addresses := %s::public.address[]
            )
        """
        params = [
            data.order_class,
            data.payment_method,
            [
                (
                    address.country,
                    address.city,
                    address.street,
                    address.house
                ) for address in data.addresses
            ]
        ]

        return db.execute(query, params=params, fetch_count=0, executor_username=user.login)

    @staticmethod
    def order_stat(order_id: int, user: TokenDataSchema = None) -> Exception | OrdersStatView:
        db = DatabaseController()

        query = """
            SELECT * FROM authorized.order_stat(
                p_order_id := %s
            )
        """
        params = [
            order_id
        ]

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def orders_history(user: TokenDataSchema = None) -> Exception | list[OrdersView]:
        db = DatabaseController()

        query = """SELECT * FROM authorized.orders_history()"""
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def rate_order(order_id: int, data: RateOrderSchema, user: TokenDataSchema = None) -> Exception | OrdersStatView:
        db = DatabaseController()

        query = """
                SELECT * FROM authorized.rate_order(
                    p_order_id := %s, 
                    p_mark := %s, 
                    p_comment := %s, 
                    p_tags := %s::public.driver_tags[]          
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

        return db.execute(query, params=params, fetch_count=0, executor_username=user.login)

    @staticmethod
    def update_profile(data: UpdateProfile, user: TokenDataSchema = None) -> Exception | UsersView:
        db = DatabaseController()

        query = """
            SELECT * FROM authorized.update_profile(
                p_first_name := %s, 
                p_last_name := %s, 
                p_email := %s, 
                p_tel_number := %s, 
                p_city_id := %s, 
                p_password := %s
            )
        """
        params = [
            data.first_name,
            data.last_name,
            data.email,
            data.tel_number,
            data.city_id,
            data.password
        ]

        return db.execute(query, params=params, fetch_count=0, executor_username=user.login)