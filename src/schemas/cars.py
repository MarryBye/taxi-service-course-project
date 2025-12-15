from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import CarClass, CarStatus, CityName, CountryName
from src.schemas.drivers import DriverSchema

class BaseCarSchema(BaseModel):
    mark: str = Field(..., alias="mark", description="Car mark", max_length=32)
    model: str = Field(..., alias="model", description="Car model", max_length=32)
    car_number: str = Field(..., alias="car_number", description="Car number", max_length=16)
    country: CountryName = Field(..., alias="country", description="Country of the car", max_length=32)
    city: CityName = Field(..., alias="city", description="City of the car", max_length=32)
    color: str = Field(..., alias="color", description="Car color", max_length=32)
    car_class: CarClass = Field(..., alias="car_class", description="Car class", max_length=32)
    car_status: CarStatus = Field(..., alias="car_status", description="Car status", max_length=32)

class CarSchema(BaseCarSchema):
    id: int = Field(..., alias="id", description="Car ID")
    created_at: datetime = Field(..., alias="created_at", description="Car created time")
    changed_at: datetime = Field(..., alias="changed_at", description="Car updated time")
    driver_id: Optional[int] = Field(None, alias="driver_id", description="Driver ID")

class CreateCarSchema(BaseCarSchema):
    driver_id: Optional[int] = Field(None, alias="driver_id", description="Driver ID")

class UpdateCarSchema(BaseModel):
    driver_id: Optional[int] = Field(None, alias="driver_id", description="Driver ID")