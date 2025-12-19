from pydantic import BaseModel, Field
from datetime import datetime
from src.enums.db import DriverCancelTags, DriverTags, OrderStatuses, CarClasses, PaymentMethods
from src.schemas.common import Address

class CancelOrderSchema(BaseModel):
    comment: str = Field(...)
    tags: list[DriverCancelTags] = Field(...)

class MakeOrderSchema(BaseModel):
    order_class: CarClasses = Field(...)
    payment_method: PaymentMethods = Field(...)
    addresses: list[Address] = Field(...)

class RateOrderSchema(BaseModel):
    mark: int = Field(...)
    comment: str = Field(...)
    tags: list[DriverTags] = Field(...)

class UpdateProfile(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    tel_number: str = Field(...)
    country_id: int = Field(...)
    city_id: int = Field(...)
    password: str = Field(...)