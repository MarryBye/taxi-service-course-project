from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from src.schemas.common import Country, City, Transaction, Route, Rating, Cancel
from src.enums.db import UserRoles, ClientTags, ClientCancelTags, Colors, CarClasses, CarStatuses, DriverTags, DriverCancelTags, OrderStatuses

class UsersView(BaseModel):
    id: int = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    tel_number: str = Field(...)

    country: Country = Field(...)
    city: City = Field(...)

    role: UserRoles = Field(...)

    payment_balance: int = Field(...)
    earning_balance: int = Field(...)

    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)

class ClientsStatView(BaseModel):
    id: int = Field(...)

    rides_count: int = Field(...)
    finished_rides_count: int = Field(...)
    canceled_rides_count: int = Field(...)
    average_distance: float = Field(...)
    max_distance: float = Field(...)
    client_rating: float = Field(...)
    all_tags: Optional[list[ClientTags | ClientCancelTags]] = Field(...)

class CarsView(BaseModel):
    id: int = Field(...)
    driver: Optional[UsersView] = Field(...)
    mark: str = Field(...)
    model: str = Field(...)
    number_plate: str = Field(...)
    country: Country = Field(...)
    city: City = Field(...)
    color: Colors = Field(...)
    car_class: CarClasses = Field(...)
    car_status: CarStatuses = Field(...)
    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)

class DriversStatView(BaseModel):
    id: int = Field(...)
    car: Optional[CarsView] = Field(...)
    rides_count: int = Field(...)
    finished_rides_count: int = Field(...)
    canceled_rides_count: int = Field(...)
    average_distance: float = Field(...)
    max_distance: float = Field(...)
    driver_rating: float = Field(...)
    all_tags: Optional[list[DriverTags | DriverCancelTags]] = Field(...)

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
    duration: Optional[int] = Field(...)

class MaintenancesView(BaseModel):
    id: int = Field(...)
    car: CarsView = Field(...)
    description: str = Field(...)
    cost: int = Field(...)
    maintenance_start: datetime = Field(...)
    maintenance_end: datetime = Field(...)
    created_at: datetime = Field(...)
    changed_at: datetime = Field(...)