from src.controllers.database import DatabaseController
from src.schemas.auth import TokenDataSchema
from src.schemas.views import *
from src.schemas.admin import *


class AdminService:
    @staticmethod
    def create_car(data: CreateCarSchema, user: TokenDataSchema = None) -> Exception | CarsView:
        db = DatabaseController()

        query = ("""
            SELECT * FROM admin.create_car(
                p_mark := %s, 
                p_model := %s, 
                p_number_plate := %s, 
                p_city_id := %s, 
                p_color := %s, 
                p_car_class := %s,
                p_car_status := %s, 
                p_driver_id := %s              
            ) 
        """)
        params = [
            data.mark,
            data.model,
            data.number_plate,
            data.city_id,
            data.color,
            data.car_class,
            data.car_status,
            data.driver_id
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def create_maintenance(data: CreateMaintenanceSchema, user: TokenDataSchema = None) -> Exception | MaintenancesView:
        db = DatabaseController()

        query = (
            """
            SELECT * FROM admin.create_maintenance(
                p_car_id := %s, 
                p_description := %s, 
                p_cost := %s, 
                p_status := %s, 
                p_maintenance_start := %s, 
                p_maintenance_end := %s
            )
            """
        )
        params = [
            data.car_id,
            data.description,
            data.cost,
            data.status,
            data.maintenance_start,
            data.maintenance_end
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def create_transaction(data: CreateTransactionSchema, user: TokenDataSchema = None) -> Exception | TransactionsView:
        db = DatabaseController()

        query = """
            SELECT * FROM admin.create_transaction(
                p_user_id := %s, 
                p_balance_type := %s, 
                p_transaction_type := %s, 
                p_payment_method := %s, 
                p_amount := %s
            )
        """
        params = [
            data.user_id,
            data.balance_type,
            data.transaction_type,
            data.payment_method,
            data.amount
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def create_user(data: CreateUserSchema, user: TokenDataSchema = None) -> Exception | UsersView:
        db = DatabaseController()

        query = """
            SELECT * FROM admin.create_user(
                p_login := %s, 
                p_password := %s, 
                p_first_name := %s, 
                p_last_name := %s, 
                p_email := %s, 
                p_tel_number := %s, 
                p_city_id := %s, 
                p_role := %s
            )
        """
        params = [
            data.login,
            data.password,
            data.first_name,
            data.last_name,
            data.email,
            data.tel_number,
            data.city_id,
            data.role
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def delete_car(car_id: int, user: TokenDataSchema = None) -> Exception | None:
        db = DatabaseController()

        query = """
            SELECT * FROM admin.delete_car(%s)
        """
        params = [car_id]

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def delete_maintenance(maintenance_id: int, user: TokenDataSchema = None) -> Exception | None:
        db = DatabaseController()

        query = """SELECT * FROM admin.delete_maintenance(%s)"""
        params = [maintenance_id]

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def delete_user(user_id: int, user: TokenDataSchema = None) -> Exception | None:
        db = DatabaseController()

        query = """SELECT * FROM admin.delete_user(%s)"""
        params = [user_id]

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def get_car(car_id: int, user: TokenDataSchema = None) -> Exception | CarsView:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_car(%s)"""
        params = [car_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def get_cars(user: TokenDataSchema = None) -> Exception | list[CarsView]:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_cars()"""
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def get_client_statistics(user_id: int, user: TokenDataSchema = None) -> Exception | ClientsStatView:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_client_statistics(%s)"""
        params = [user_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def get_driver_statistics(user_id: int, user: TokenDataSchema = None) -> Exception | DriversStatView:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_driver_statistics(%s)"""
        params = [user_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def get_maintenance(maintenance_id: int, user: TokenDataSchema = None) -> Exception | MaintenancesView:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_maintenance(%s)"""
        params = [maintenance_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def get_maintenances(user: TokenDataSchema = None) -> Exception | list[MaintenancesView]:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_maintenances()"""
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def get_order(order_id: int, user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_order(%s)"""
        params = [order_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def get_order_statistics(order_id: int, user: TokenDataSchema = None) -> Exception | OrdersStatView:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_order_statistics(%s)"""
        params = [order_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def get_orders(user: TokenDataSchema = None) -> Exception | list[OrdersView]:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_orders()"""
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def get_transaction(transaction_id: int, user: TokenDataSchema = None) -> Exception | TransactionsView:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_transaction(%s)"""
        params = [transaction_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def get_transactions(user: TokenDataSchema = None) -> Exception | list[TransactionsView]:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_transactions()"""
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def get_user(user_id: int, user: TokenDataSchema = None) -> Exception | UsersView:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_user(%s)"""
        params = [user_id]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def get_users(user: TokenDataSchema = None) -> Exception | list[UsersView]:
        db = DatabaseController()

        query = """SELECT * FROM admin.get_users()"""
        params = []

        return db.execute(query, params=params, fetch_count=-1, executor_username=user.login)

    @staticmethod
    def update_car(car_id: int, data: UpdateCarSchema, user: TokenDataSchema = None) -> Exception | CarsView:
        db = DatabaseController()

        query = """
                SELECT * FROM admin.update_car(
                    p_car_id := %s, 
                    p_mark := %s, 
                    p_model := %s, 
                    p_number_plate := %s, 
                    p_city_id := %s, 
                    p_color := %s, 
                    p_car_class := %s, 
                    p_car_status := %s, 
                    p_driver_id := %s
                )
        """
        params = [
            car_id,
            data.mark,
            data.model,
            data.number_plate,
            data.city_id,
            data.color,
            data.car_class,
            data.car_status,
            data.driver_id
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def update_maintenance(maintenance_id: int, data: UpdateMaintenanceSchema, user: TokenDataSchema = None) -> Exception | MaintenancesView:
        db = DatabaseController()

        query = """
            SELECT * FROM admin.update_maintenance(
                p_maintenance_id := %s, 
                p_status := %s
            )
        """
        params = [
            maintenance_id,
            data.status
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def update_order(order_id: int, data: UpdateOrderSchema, user: TokenDataSchema = None) -> Exception | OrdersView:
        db = DatabaseController()

        query = """
            SELECT * FROM admin.update_order(
                p_order_id := %s, 
                p_status := %s, 
                p_order_class := %s
            )
        """
        params = [
            order_id,
            data.status,
            data.order_class
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)

    @staticmethod
    def update_user(user_id: int, data: UpdateUserSchema, user: TokenDataSchema = None) -> Exception | UsersView:
        db = DatabaseController()

        query = """
            SELECT * FROM admin.update_user(
                p_user_id := %s, 
                p_first_name := %s, 
                p_last_name := %s, 
                p_email := %s, 
                p_tel_number := %s, 
                p_city_id := %s, 
                p_role := %s
            )
        """
        params = [
            user_id,
            data.first_name,
            data.last_name,
            data.email,
            data.tel_number,
            data.city_id,
            data.role
        ]

        return db.execute(query, params=params, fetch_count=1, executor_username=user.login)