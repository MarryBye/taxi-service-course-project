from datetime import datetime
from pydantic import BaseModel, Field
from src.enums.car_class_enum import CarClassEnum
from src.enums.car_status_enum import CarStatusEnum

class CarBaseSchema(BaseModel):
    car_number: str
    driver_id: int | None
    car_class: CarClassEnum
    car_status: CarStatusEnum
    mark: str
    model: str

class CarSchema(CarBaseSchema):
    id: int

class CarCreateSchema(CarBaseSchema):
    pass

class CarUpdateSchema(BaseModel):
    car_number: str | None
    driver_id: int | None
    car_class: CarClassEnum | None
    car_status: CarStatusEnum | None
    mark: str | None
    model: str | None

class CarDeleteSchema(BaseModel):
    id: int
