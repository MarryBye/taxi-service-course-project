from src.services.base_service import BaseService
from src.database.controller import database

class UsersService(BaseService):
    @staticmethod
    def list():
        query = "SELECT * FROM users_view;"
        return database.execute(query, fetch_count=-1)
    
    @staticmethod
    def list_drivers():
        query = "SELECT * FROM drivers_view;"
        return database.execute(query, fetch_count=-1)
    
    @staticmethod
    def get(id: int):
        query = "SELECT * FROM users_view WHERE id = %s;"
        return database.execute(query, params=[id], fetch_count=1)  
    
    @staticmethod
    def get_driver(id: int):
        query = "SELECT * FROM drivers_view WHERE id = %s;"
        return database.execute(query, params=[id], fetch_count=1)
    
    @staticmethod
    def create(login, email, tel_number, password, first_name, last_name, role):
        query = "SELECT * FROM create_user(%s, %s, %s, %s, %s, %s, %s);"
        params = [login, email, tel_number, password, first_name, last_name, role] 
        return database.execute(query, params=params, fetch_count=1)
    
    @staticmethod
    def update(id: int, email = None, tel_number = None, password = None, first_name = None, last_name = None, role = None):
        query = "SELECT * FROM update_user(%s, %s, %s, %s, %s, %s, %s);"
        params = [id, email, tel_number, password, first_name, last_name, role]
        return database.execute(query, params=params, fetch_count=1)
        
    @staticmethod
    def delete(id: int):
        query = "CALL delete_user(%s);"
        return database.execute(query, params=[id], fetch_count=0)
    
    @staticmethod
    def auth(login: str):
        query = "SELECT * FROM auth_user(%s);"
        return database.execute(query, params=[login], fetch_count=1)