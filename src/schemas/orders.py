from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import OrderStatus, CarClass, PaymentMethod
from src.schemas.common import AddressSchema
from src.schemas.mixins.hashable_password import WithHashablePassword
from src.schemas.users import *

class BaseOrderSchema(BaseModel):
    client_id: int = Field(..., alias="client_id", description="Client ID")
    driver_id: Optional[int] = Field(None, alias="driver_id", description="Driver ID")
    transaction_id: Optional[int] = Field(None, alias="transaction_id", description="Transaction ID")
    status: OrderStatus = Field(..., alias="status", description="Order status")
    order_class: CarClass = Field(..., alias="order_class", description="Order class")

class OrderSchema(BaseOrderSchema):
    id: int = Field(..., alias="id", description="Order ID")
    created_at: datetime = Field(..., alias="created_at", description="Order created time")
    changed_at: datetime = Field(..., alias="changed_at", description="Order updated time")
    client_rating_id: Optional[int] = Field(None, alias="client_rating_id", description="Client rating ID")
    driver_rating_id: Optional[int] = Field(None, alias="driver_rating_id", description="Driver rating ID")
    cancel_id: Optional[int] = Field(None, alias="cancel_id", description="Cancel ID")
    route_id: Optional[int] = Field(None, alias="route_id", description="Route ID")

class AdminCreateOrderSchema(BaseModel):
    client_id: int = Field(..., alias="client_id", description="Client ID")
    status: OrderStatus = Field(..., alias="status", description="Order status")
    order_class: CarClass = Field(..., alias="order_class", description="Order class")
    payment_method: PaymentMethod = Field(..., alias="payment_method", description="Payment method")
    amount: int = Field(..., alias="amount", description="Order amount")
    addresses: list[AddressSchema] = Field(..., alias="addresses", description="Order addresses")
    driver_id: Optional[int] = Field(None, alias="driver_id", description="Driver ID")

class MakeOrderSchema(BaseModel):
    order_class: CarClass = Field(..., alias="order_class", description="Order class")
    payment_method: PaymentMethod = Field(..., alias="payment_method", description="Payment method")
    amount: int = Field(..., alias="amount", description="Order amount")
    addresses: list[AddressSchema] = Field(..., alias="addresses", description="Order addresses")

class AdminUpdateOrderSchema(BaseModel):
    status: OrderStatus = Field(..., alias="status", description="Order status")
    order_class: CarClass = Field(..., alias="order_class", description="Order class")