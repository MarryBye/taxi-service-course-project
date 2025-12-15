from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import UserRole, CountryName, CityName, ClientTag
from src.schemas.mixins.hashable_password import WithHashablePassword
from src.schemas.users import *

class ClientSchema(UserSchema):
    payment_balance: int = Field(..., alias="payment_balance", description="Client's payment balance")
    rides_count: int = Field(..., alias="rides_count", description="Client's rides count")
    finished_rides_count: int = Field(..., alias="finished_rides_count", description="Client's finished rides count")
    canceled_rides_count: int = Field(..., alias="canceld_rides_count", description="Client's canceld rides count")
    average_distance: float = Field(..., alias="average_distance", description="Client's average distance")
    max_distance: float = Field(..., alias="max_distance", description="Client's max distance")
    client_rating: float = Field(..., alias="client_rating", description="Client's rating")
    most_popular_tag: ClientTag = Field(..., alias="most_popular_tag", description="Client's most popular tag")