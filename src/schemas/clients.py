from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import DriverCancelTag, CarClass, PaymentMethod, ClientTag, CountryName, CityName, DriverTag
from src.schemas.common import AddressSchema
from src.schemas.mixins.hashable_password import WithHashablePassword
from src.schemas.users import UserSchema

class CancelOrderSchema(BaseModel):
    comment: str = Field(..., alias="comment", description="Comment about the order cancellation")
    driver_tags: list[DriverCancelTag] = Field(..., alias="driver_tags", description="Driver tags")

class MakeOrderSchema(BaseModel):
    order_class: CarClass = Field(..., alias="order_class", description="Order class")
    payment_method: PaymentMethod = Field(..., alias="payment_method", description="Payment method")
    amount: int = Field(..., alias="amount", description="Order amount")
    addresses: list[AddressSchema] = Field(..., alias="addresses", description="Order addresses")

class RateOrderSchema(BaseModel):
    mark: int = Field(..., alias="mark", description="Order rating mark")
    comment: Optional[str] = Field(None, alias="comment", description="Order rating comment")
    driver_tags: list[DriverTag] = Field(..., alias="driver_tags", description="Driver tags")

class UpdateProfileSchema(BaseModel, WithHashablePassword):
    email: Optional[str] = Field(None, alias="email", description="Email address of the user", max_length=128)
    tel_number: Optional[str] = Field(None, alias="tel_number", description="Telephone number of the user", max_length=32)
    password: Optional[str] = Field(None, alias="password", description="User's password")
    first_name: Optional[str] = Field(None, alias="first_name", description="First name of the user", max_length=32)
    last_name: Optional[str] = Field(None, alias="last_name", description="Last name of the user", max_length=32)
    country: Optional[CountryName] = Field(None, alias="country", description="Country of the user", max_length=32)
    city: Optional[CityName] = Field(None, alias="city", description="City of the user", max_length=32)

class ClientSchema(UserSchema):
    payment_balance: Optional[int] = Field(..., alias="payment_balance", description="Client's payment balance")
    rides_count: Optional[int] = Field(..., alias="rides_count", description="Client's rides count")
    finished_rides_count: Optional[int] = Field(..., alias="finished_rides_count", description="Client's finished rides count")
    canceled_rides_count: Optional[int] = Field(..., alias="canceled_rides_count", description="Client's canceld rides count")
    average_distance: Optional[float] = Field(..., alias="average_distance", description="Client's average distance")
    max_distance: Optional[float] = Field(..., alias="max_distance", description="Client's max distance")
    client_rating: Optional[float] = Field(..., alias="client_rating", description="Client's rating")
    most_popular_tag: Optional[ClientTag] = Field(..., alias="most_popular_tag", description="Client's most popular tag")