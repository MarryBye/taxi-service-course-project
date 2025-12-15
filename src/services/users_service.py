from src.controllers.database import Database
from src.schemas.auth import AuthUserSchema
from src.schemas.users import AdminCreateUserSchema, UpdateUserSchema
from src.schemas.token import TokenDataSchema
from src.enums.db import UserRole

class UsersService:
    @staticmethod
    def list(limit: int = 10, offset: int = 0, user: TokenDataSchema = None):
        db =  Database(user=user)
        query = """SELECT * FROM list_users(%s, %s)"""
        params = [limit, offset]
        return db.execute(query, params=params, fetch_count=-1)
    
    @staticmethod
    def get(id: int, executor: AuthUserSchema = None):
        query = "SELECT * FROM get_user(%s)"
        return database.execute(query, params=[id], fetch_count=1, executor_data=executor)
    
    @staticmethod
    def create(schema: CreateUserSchema, executor: AuthUserSchema = None):
        query = "SELECT * FROM create_user(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = [
            schema.login,
            schema.email,
            schema.tel_number,
            schema.password,
            schema.first_name,
            schema.last_name,
            schema.city_name,
            schema.country_name,
            schema.role
        ]
        return database.execute(query, params=params, fetch_count=1, executor_data=executor)
    
    @staticmethod
    def update(id: int, schema: UpdateUserSchema, executor: AuthUserSchema = None):
        query = "SELECT * FROM update_user(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = [
            id,
            schema.email,
            schema.tel_number,
            schema.first_name,
            schema.last_name,
            schema.password,
            schema.role,
            schema.city_name,
            schema.country_name
        ]
        return database.execute(query, params=params, fetch_count=1, executor_data=executor)
        
    @staticmethod
    def delete(id: int, executor: AuthUserSchema = None):
        query = "SELECT * FROM delete_user(%s)"
        return database.execute(query, params=[id], fetch_count=0, executor_data=executor)

    @staticmethod
    def get_role(login: str, executor: AuthUserSchema = None):
        query = "SELECT rolname FROM get_role(%s)"
        return database.execute(query, params=[login], fetch_count=1, executor_data=executor)