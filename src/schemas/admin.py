from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from src.enums.db import *
from src.schemas.common import *
from src.schemas.views import *

class CreateCarSchema(BaseModel):
    mark: str = Field(...)
    model: str = Field(...)
    number_plate: str = Field(...)
    city_id: int = Field(...)
    color: Colors = Field(...)
    car_class: CarClasses = Field(...)
    car_status: CarStatuses = Field(...)
    driver_id: Optional[int] = Field(...)

class UpdateCarSchema(BaseModel):
    mark: Optional[str] = Field(...)
    model: Optional[str] = Field(...)
    number_plate: Optional[str] = Field(...)
    city_id: Optional[int] = Field(...)
    color: Optional[Colors] = Field(...)
    car_class: CarClasses = Field(...)
    car_status: CarStatuses = Field(...)
    driver_id: Optional[int] = Field(...)

class CreateMaintenanceSchema(BaseModel):
    car_id: int = Field(...)
    description: str = Field(...)
    cost: int = Field(...)
    status: MaintenanceStatuses = Field(...)
    maintenance_start: datetime = Field(...)
    maintenance_end: datetime = Field(...)

class UpdateMaintenanceSchema(BaseModel):
    status: Optional[MaintenanceStatuses] = Field(...)

class CreateTransactionSchema(BaseModel):
    user_id: int = Field(...)
    balance_type: BalanceTypes = Field(...)
    transaction_type: TransactionType = Field(...)
    payment_method: PaymentMethods = Field(...)
    amount: int = Field(...)

class CreateUserSchema(BaseModel):
    login: str = Field(...)
    password: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    tel_number: str = Field(...)
    city_id: int = Field(...)
    role: UserRoles = Field(...)

class UpdateUserSchema(BaseModel):
    first_name: Optional[str] = Field(...)
    last_name: Optional[str] = Field(...)
    email: Optional[str] = Field(...)
    tel_number: Optional[str] = Field(...)
    city_id: int = Field(...)
    role: Optional[UserRoles] = Field(...)

class UpdateOrderSchema(BaseModel):
    status: OrderStatuses = Field(...)
    order_class: CarClasses = Field(...)