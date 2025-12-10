from src.services.base_service import BaseService
from src.database.controller import database

class DriversService(BaseService):
    @staticmethod
    def list(limit: int = 10, offset: int = 0):
        query = "SELECT * FROM list_drivers(limit_number := %s, offset_number := %s);"
        params = [limit, offset]
        return database.execute(query, params=params, fetch_count=-1)

    @staticmethod
    def get(id: int):
        query = "SELECT * FROM get_driver(%s);"
        return database.execute(query, params=[id], fetch_count=1)

    @staticmethod
    def create(login, email, tel_number, password, first_name, last_name, city_name, country_name):
        query = "SELECT * FROM create_user(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        params = [login, email, tel_number, password, first_name, last_name, 'driver', city_name, country_name]
        return database.execute(query, params=params, fetch_count=1)

    @staticmethod
    def update(id: int, email=None, tel_number=None, password=None, first_name=None, last_name=None, city_name=None, country_name=None):
        query = "SELECT * FROM update_user(%s, %s, %s, %s, %s, %s, %s, %s);"
        params = [id, email, tel_number, password, first_name, last_name, city_name, country_name]
        return database.execute(query, params=params, fetch_count=1)

    @staticmethod
    def delete(id: int):
        query = "CALL delete_user(%s);"
        return database.execute(query, params=[id], fetch_count=0)