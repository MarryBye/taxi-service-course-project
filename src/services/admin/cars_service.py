from src.controllers.database import Database
from src.schemas.token import TokenDataSchema
from src.schemas.cars import CreateCarSchema, UpdateCarSchema


class CarsService:
    @staticmethod
    def list(limit: int = 10, offset: int = 0, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "SELECT * FROM admin.list_cars(%s, %s)"
        return db.execute(query, params=[offset, limit], fetch_count=-1)

    @staticmethod
    def get(car_id: int, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "SELECT * FROM admin.get_car(%s)"
        return db.execute(query, params=[car_id], fetch_count=1)

    @staticmethod
    def create(schema: CreateCarSchema, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.create_car(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def update(car_id: int, schema: UpdateCarSchema, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.update_car(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def delete(car_id: int, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.delete_car(%s)"
        return db.execute(query, params=[car_id], fetch_count=0)
