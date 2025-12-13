from src.controllers.database import database
from src.schemas.auth import AuthUserSchema
from src.schemas.users import CreateUserSchema, UpdateUserSchema
from src.enums.roles import UserRole

class UsersService:
    @staticmethod
    def list(limit: int = 10, offset: int = 0, executor: AuthUserSchema = None, **kwargs):
        query = """SELECT * FROM admin.users_view LIMIT %s OFFSET %s"""



        params = [limit, offset]
        return database.execute(query, params=params, fetch_count=-1, executor_data=executor)
    
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