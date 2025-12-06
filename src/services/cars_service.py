from src.services.base_service import BaseService
from src.database.controller import database

class CarsService(BaseService):
    @staticmethod
    def list():
        query = "SELECT * FROM cars_view;"
        return database.execute(query, fetch_count=-1)
    
    @staticmethod
    def get(id: int):
        query = "SELECT * FROM cars_view WHERE id = %s;"
        return database.execute(query, params=[id], fetch_count=1)  
    
    @staticmethod
    def create(mark, model, car_number, car_class, car_status, driver_id=None):
        query = "SELECT * FROM create_car(%s, %s, %s, %s, %s, %s);"
        params = [mark, model, car_number, car_class, car_status, driver_id]
        return database.execute(query, params=params, fetch_count=1)
    
    @staticmethod
    def update(id: int, mark, model, car_number, car_class, car_status, driver_id=None):
        query = "SELECT * FROM update_car(%s, %s, %s, %s, %s, %s, %s);"
        params = [id, mark, model, car_number, car_class, car_status, driver_id]
        return database.execute(query, params=params, fetch_count=1)
        
    @staticmethod
    def delete(id: int):
        query = "CALL delete_car(%s);"
        return database.execute(query, params=[id], fetch_count=0)