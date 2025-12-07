from src.services.base_service import BaseService
from src.database.controller import database

class OrdersService(BaseService):
    @staticmethod
    def list():
        query = "SELECT * FROM orders_view;"
        return database.execute(query, fetch_count=-1)
    
    @staticmethod
    def get(id: int):
        query = "SELECT * FROM orders_view WHERE id = %s;"
        return database.execute(query, params=[id], fetch_count=1)  
    
    @staticmethod
    def get_client_orders(client_id: int):
        query = "SELECT * FROM orders_view WHERE (client->>'id')::int = %s;"
        return database.execute(query, params=[client_id], fetch_count=-1)
    
    @staticmethod
    def get_driver_orders(driver_id: int):
        query = "SELECT * FROM orders_view WHERE (driver->>'id')::int = %s;"
        return database.execute(query, params=[driver_id], fetch_count=-1)
    
    @staticmethod
    def create(client_id: int, driver_id: int | None = None, status: str = 'searching_for_driver'):
        query = "SELECT * FROM create_order(%s, %s, %s);"
        params = [client_id, driver_id, status] 
        return database.execute(query, params=params, fetch_count=1)
    
    @staticmethod
    def update(id: int, driver_id: int | None = None, status: str | None = None, finished_at: str | None = None):
        query = "SELECT * FROM update_order(%s, %s, %s, %s);"
        params = [id, driver_id, status, finished_at]
        return database.execute(query, params=params, fetch_count=1)
        
    @staticmethod
    def delete(id: int):
        query = "CALL delete_order(%s);"
        return database.execute(query, params=[id], fetch_count=0)