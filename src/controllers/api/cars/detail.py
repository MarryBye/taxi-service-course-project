from fastapi import HTTPException, status
from src.schemas.car import CarSchema
from src.database.controller import database

def detail_view(car_id: int) -> CarSchema:
    car = database.execute('SELECT * FROM get_car(%s)', [car_id], fetch_count=1)
    return car