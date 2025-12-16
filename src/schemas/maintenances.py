from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import MaintenanceStatus
from src.schemas.common import AddressSchema
from src.schemas.mixins.hashable_password import WithHashablePassword
from src.schemas.users import *

class BaseMaintenanceSchema(BaseModel):
    car_id: int = Field(..., alias="car_id", description="Maintenance's car ID")
    description: str = Field(..., alias="description", description="Maintenance's description")
    cost: int = Field(..., alias="cost", description="Maintenance's cost")
    status: MaintenanceStatus = Field(..., alias="status", description="Maintenance's status")
    maintenance_start: datetime = Field(..., alias="maintenance_start", description="Maintenance's start time")
    maintenance_end: datetime = Field(..., alias="maintenance_end", description="Maintenance's end time")

class MaintenanceSchema(BaseMaintenanceSchema):
    id: int = Field(..., alias="id", description="Maintenance ID")
    created_at: datetime = Field(..., alias="created_at", description="Maintenance created time")
    changed_at: datetime = Field(..., alias="changed_at", description="Maintenance updated time")

class CreateMaintenanceSchema(BaseMaintenanceSchema):
    car_id: int = Field(..., alias="car_id", description="Maintenance's car ID")
    description: str = Field(..., alias="description", description="Maintenance's description")
    cost: int = Field(..., alias="cost", description="Maintenance's cost")
    status: MaintenanceStatus = Field(..., alias="status", description="Maintenance's status")

class UpdateMaintenanceSchema(BaseModel):
    description: Optional[str] = Field(None, alias="description", description="Maintenance's description")
    cost: Optional[int] = Field(None, alias="cost", description="Maintenance's cost")
    status: Optional[MaintenanceStatus] = Field(None, alias="status", description="Maintenance's status")
