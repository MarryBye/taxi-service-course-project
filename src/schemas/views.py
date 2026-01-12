from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Optional, Union
from src.schemas.common import Country, City, Transaction, Route, Rating, Cancel
from src.enums.db import UserRoles, ClientTags, ClientCancelTags, Colors, CarClasses, CarStatuses, DriverTags, \
    DriverCancelTags, OrderStatuses, TransactionType, BalanceTypes, PaymentMethods, MaintenanceStatuses


class UsersView(BaseModel):
    id: int = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    tel_number: str = Field(...)

    city: City = Field(...)

    role: UserRoles = Field(...)

    payment_balance: int = Field(...)
    earning_balance: int = Field(...)

    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)

class CarsUserView(BaseModel):
    id: int = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    tel_number: str = Field(...)

    role: UserRoles = Field(...)

    payment_balance: int = Field(...)
    earning_balance: int = Field(...)

    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)

class ClientStatTags(BaseModel):
    tag: Union[ClientTags, DriverCancelTags] = Field(...)
    count: int = Field(...)

class DriverStatTags(BaseModel):
    tag: Union[DriverTags, ClientCancelTags] = Field(...)
    count: int = Field(...)

class ClientsStatView(BaseModel):
    id: int = Field(...)

    rides_count: int = Field(...)
    finished_rides_count: int = Field(...)
    canceled_rides_count: int = Field(...)
    average_distance: Optional[float] = Field(...)
    max_distance: Optional[float] = Field(...)
    client_rating: Optional[float] = Field(...)
    all_tags: Optional[list[ClientStatTags]] = Field(...)

class CarsView(BaseModel):
    id: int = Field(...)
    driver: Optional[CarsUserView] = Field(...)
    mark: str = Field(...)
    model: str = Field(...)
    number_plate: str = Field(...)
    city: City = Field(...)
    color: Colors = Field(...)
    car_class: CarClasses = Field(...)
    car_status: CarStatuses = Field(...)
    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)

class DriverStatCar(BaseModel):
    id: int = Field(...)
    mark: str = Field(...)
    model: str = Field(...)
    number_plate: str = Field(...)
    color: Colors = Field(...)
    car_class: CarClasses = Field(...)
    car_status: CarStatuses = Field(...)
    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)

class DriversStatView(BaseModel):
    id: int = Field(...)
    car: Optional[DriverStatCar] = Field(...)
    rides_count: int = Field(...)
    finished_rides_count: int = Field(...)
    canceled_rides_count: int = Field(...)
    average_distance: Optional[float] = Field(...)
    max_distance: Optional[float] = Field(...)
    driver_rating: Optional[float] = Field(...)
    all_tags: Optional[list[DriverStatTags]] = Field(...)

class OrdersView(BaseModel):
    id: int = Field(...)
    client: UsersView = Field(...)
    driver: Optional[UsersView] = Field(...)
    transaction: Transaction = Field(...)
    route: Route = Field(...)
    status: OrderStatuses = Field(...)
    order_class: CarClasses = Field(...)
    finished_at: Optional[datetime] = Field(...)
    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)

class OrdersStatView(BaseModel):
    id: int = Field(...)
    rating_by_client: Optional[Rating] = Field(...)
    rating_by_driver: Optional[Rating] = Field(...)
    cancel_info: Optional[Cancel] = Field(...)
    duration: Optional[timedelta] = Field(...)

class MaintenancesView(BaseModel):
    id: int = Field(...)
    car: CarsView = Field(...)
    description: str = Field(...)
    cost: int = Field(...)
    maintenance_start: datetime = Field(...)
    maintenance_end: datetime = Field(...)
    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)
    status: MaintenanceStatuses = Field(...)

class TransactionsView(BaseModel):
    id: int = Field(...)
    user: UsersView = Field(...)
    balance_type: BalanceTypes = Field(...)
    transaction_type: TransactionType = Field(...)
    payment_method: PaymentMethods = Field(...)
    amount: int = Field(...)
    created_at: datetime = Field(...)