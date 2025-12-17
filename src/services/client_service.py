from src.controllers.database import Database
from src.schemas.clients import CancelOrderSchema, MakeOrderSchema, RateOrderSchema, UpdateProfileSchema
from src.schemas.token import TokenDataSchema


class ClientService:
    @staticmethod
    def cancel_current_order(schema: CancelOrderSchema, user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL authorized.cancel_current_order(%s, %s, %s)"
        params = [
            user.id,
            schema.comment,
            schema.driver_tags
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def get_client_history(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "SELECT * FROM authorized.get_client_history(%s)"
        params = [
            user.id
        ]

        return db.execute(query, params=params, fetch_count=-1)

    @staticmethod
    def get_current_order(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "SELECT * FROM authorized.get_current_order(%s)"
        params = [user.id]

        return db.execute(query, params=params, fetch_count=1)

    @staticmethod
    def get_profile(user: TokenDataSchema = None):
        db = Database(user=user)

        query = "SELECT * FROM authorized.get_profile(%s)"
        params = [user.id]

        return db.execute(query, params=params, fetch_count=1)

    @staticmethod
    def make_order(schema: MakeOrderSchema, user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL authorized.make_order(%s, %s, %s, %s, %s)"
        params = [
            user.id,
            schema.order_class,
            schema.payment_method,
            schema.amount,
            schema.address
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def rate_order_by_client(schema: RateOrderSchema, user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL authorized.rate_order_by_client(%s, %s, %s, %s)"
        params = [
            user.id,
            schema.mark,
            schema.comment,
            schema.driver_tags
        ]

        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def update_profile(schema: UpdateProfileSchema, user: TokenDataSchema = None):
        db = Database(user=user)

        query = "CALL authorized.update_profile(%s, %s, %s, %s, %s, %s, %s, %s)"
        params = [
            user.id,
            schema.email,
            schema.tel_number,
            schema.password,
            schema.first_name,
            schema.last_name,
            schema.country,
            schema.city
        ]

        return db.execute(query, params=params, fetch_count=0)