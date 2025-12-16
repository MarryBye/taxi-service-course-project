from src.controllers.database import Database
from src.schemas.users import AdminCreateUserSchema, AdminUpdateUserSchema
from src.schemas.token import TokenDataSchema

class UsersService:
    @staticmethod
    def list(limit: int = 10, offset: int = 0, user: TokenDataSchema = None):
        db =  Database(user=user)
        query = """SELECT * FROM admin.list_users(%s, %s)"""
        params = [offset, limit]
        return db.execute(query, params=params, fetch_count=-1)
    
    @staticmethod
    def get(id: int, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "SELECT * FROM admin.get_user(%s)"
        return db.execute(query, params=[id], fetch_count=1)
    
    @staticmethod
    def create(schema: AdminCreateUserSchema, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.create_user(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = [
            schema.login,
            schema.email,
            schema.tel_number,
            schema.password,
            schema.first_name,
            schema.last_name,
            schema.country,
            schema.city,
            schema.role
        ]
        return db.execute(query, params=params, fetch_count=0)
    
    @staticmethod
    def update(id: int, schema: AdminUpdateUserSchema, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.update_user(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = [
            id,
            schema.email,
            schema.tel_number,
            schema.password,
            schema.first_name,
            schema.last_name,
            schema.country_name,
            schema.city_name,
            schema.role
        ]
        return db.execute(query, params=params, fetch_count=1)
        
    @staticmethod
    def delete(id: int, user: TokenDataSchema = None):
        db = Database(user=user)
        query = "CALL admin.delete_user(%s)"
        return db.execute(query, params=[id], fetch_count=0)