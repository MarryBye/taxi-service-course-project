from src.controllers.database import database
from src.schemas.auth import AuthUserSchema
from src.schemas.maintenance import CreateMaintenanceSchema, UpdateMaintenanceSchema


class MaintenanceService:
    @staticmethod
    def list(limit: int = 10, offset: int = 0, executor: AuthUserSchema = None):
        query = "SELECT * FROM admin.list_maintenances(%s, %s)"
        return database.execute(query, params=[offset, limit], fetch_count=-1, executor_data=executor)

    @staticmethod
    def get(id: int, executor: AuthUserSchema = None):
        query = "SELECT * FROM admin.get_maintenance(%s)"
        return database.execute(query, params=[id], fetch_count=1, executor_data=executor)

    @staticmethod
    def create(schema: CreateMaintenanceSchema, executor: AuthUserSchema = None):
        query = "CALL admin.create_maintenance(%s, %s, %s, %s)"
        params = [
            schema.car_id,
            schema.description,
            schema.cost,
            schema.status
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)

    @staticmethod
    def update(id: int, schema: UpdateMaintenanceSchema, executor: AuthUserSchema = None):
        query = "CALL admin.update_maintenance(%s, %s, %s, %s)"
        params = [
            id,
            schema.description,
            schema.cost,
            schema.status
        ]
        return database.execute(query, params=params, fetch_count=0, executor_data=executor)

    @staticmethod
    def delete(id: int, executor: AuthUserSchema = None):
        query = "CALL admin.delete_maintenance(%s)"
        return database.execute(query, params=[id], fetch_count=0, executor_data=executor)
