from src.controllers.database import Database
from src.schemas.maintenances import MaintenanceSchema, CreateMaintenanceSchema, UpdateMaintenanceSchema
from src.schemas.token import TokenDataSchema


class MaintenanceService:
    @staticmethod
    def list(limit: int = 10, offset: int = 0, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "SELECT * FROM admin.list_maintenances(%s, %s)"
        params = [offset, limit]
        return db.execute(query, params=params, fetch_count=-1)

    @staticmethod
    def get(id: int, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "SELECT * FROM admin.get_maintenance(%s)"
        return db.execute(query, params=[id], fetch_count=1)

    @staticmethod
    def create(schema: CreateMaintenanceSchema, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.create_maintenance(%s, %s, %s, %s)"
        params = [
            schema.car_id,
            schema.description,
            schema.cost,
            schema.status
        ]
        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def update(id: int, schema: UpdateMaintenanceSchema, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.update_maintenance(%s, %s, %s)"
        params = [
            id,
            schema.description,
            schema.cost,
            schema.status
        ]
        return db.execute(query, params=params, fetch_count=0)

    @staticmethod
    def delete(id: int, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.delete_maintenance(%s)"
        return db.execute(query, params=[id], fetch_count=0)