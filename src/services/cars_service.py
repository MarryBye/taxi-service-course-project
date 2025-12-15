from src.controllers.database import database
from src.schemas.auth import AuthUserSchema
from src.schemas.cars import CreateCarSchema, UpdateCarSchema


class CarsService:
    @staticmethod
    def list(limit: int = 10, offset: int = 0, executor: AuthUserSchema = None):
        query = "SELECT * FROM admin.list_cars(%s, %s)"
        return database.execute(query, params=[offset, limit], fetch_count=-1, executor_data=executor)

    @staticmethod
    def get(car_id: int, executor: AuthUserSchema = None):
        query = "SELECT * FROM admin.get_car(%s)"
        return database.execute(query, params=[car_id], fetch_count=1, executor_data=executor)

    @staticmethod
    def create(schema: CreateCarSchema, executor: AuthUserSchema = None):
        query = """
            CALL admin.create_car(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = [
            schema.mark,
            schema.model,
            schema.car_number,
            schema.country,
            schema.city,
            schema.color,
            schema.car_class,
            schema.car_status,
            schema.driver_id
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)

    @staticmethod
    def update(car_id: int, schema: UpdateCarSchema, executor: AuthUserSchema = None):
        query = """
            CALL admin.update_car(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = [
            car_id,
            schema.driver_id,
            schema.mark,
            schema.model,
            schema.car_number,
            schema.country,
            schema.city,
            schema.color,
            schema.car_class,
            schema.car_status
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)

    @staticmethod
    def delete(car_id: int, executor: AuthUserSchema = None):
        query = "CALL admin.delete_car(%s)"
        return database.execute(query, params=[car_id], fetch_count=0, executor_data=executor)
