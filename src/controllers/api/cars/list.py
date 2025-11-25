from fastapi import HTTPException, status
from src.database.controller import database
from src.schemas.car import CarSchema

async def list_view() -> list[CarSchema]:
    cars = database.execute('SELECT * FROM list_cars()', fetch_count=-1)
    return cars