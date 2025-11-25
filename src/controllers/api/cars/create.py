from fastapi import HTTPException, status
from src.schemas.car import CarCreateSchema, CarSchema
from src.database.controller import database

async def create_view(schema: CarCreateSchema) -> CarSchema:
    new_car = database.execute('SELECT * FROM insert_car(%s, %s, %s, %s, %s, %s)', [
        schema.driver_id, schema.mark, schema.model, schema.car_number, schema.car_class, schema.car_status
    ], fetch_count=1)
    return new_car
