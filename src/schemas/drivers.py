from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import UserRole, CountryName, CityName, DriverTag
from src.schemas.mixins.hashable_password import WithHashablePassword
from src.schemas.users import *

class DriverSchema(UserSchema):
    earning_balance: int = Field(..., alias="earning_balance", description="Driver's earning balance")
    payment_balance: int = Field(..., alias="payment_balance", description="Driver's payment balance")
    car_id: int = Field(..., alias="car_id", description="Driver's car ID")
    rides_count: int = Field(..., alias="rides_count", description="Driver's rides count")
    finished_rides_count: int = Field(..., alias="finished_rides_count", description="Driver's finished rides count")
    canceled_rides_count: int = Field(..., alias="canceld_rides_count", description="Driver's canceld rides count")
    average_distance: float = Field(..., alias="average_distance", description="Driver's average distance")
    max_distance: float = Field(..., alias="max_distance", description="Driver's max distance")
    driver_rating: float = Field(..., alias="driver_rating", description="Driver's rating")
    most_popular_tag: DriverTag = Field(..., alias="most_popular_tag", description="Driver's most popular tag")
