from fastapi import HTTPException, status
from src.schemas.car import CarDeleteSchema, CarSchema
from src.database.controller import database

def delete_view(car_id: int):
    deleted_car = database.execute('SELECT * FROM delete_car(%s)', [car_id], fetch_count=1)
    return deleted_car