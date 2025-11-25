from fastapi import HTTPException, status
from src.schemas.car import CarUpdateSchema, CarSchema
from src.database.controller import database

def update_view(car_id: int, schema: CarUpdateSchema) -> CarSchema:
    updated_car = database.execute('SELECT * FROM update_car(%s, %s, %s, %s, %s, %s, %s)', [
        car_id, schema.driver_id, schema.mark, schema.model, schema.car_number, schema.car_class, schema.car_status
    ], fetch_count=1)
    return updated_car