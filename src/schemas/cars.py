from pydantic import BaseModel, Field
from datetime import datetime
from src.schemas.users import UserSchema
from src.enums.car_statuses import CarStatus
from src.enums.car_classes import CarClass

class BaseCarSchema(BaseModel):
    mark: str = Field(..., title="Car Mark")
    model: str = Field(..., title="Car Model")
    car_number: str = Field(..., title="Car Number")
    car_class: CarClass = Field(..., title="Car Class")
    car_status: CarStatus = Field(..., title="Car Status")

class CarCreateSchema(BaseCarSchema):
    driver_id: int | None = Field(None, title="Driver ID")
    
class CarUpdateSchema(BaseModel):
    mark: str | None = Field(None, title="Car Mark")
    model: str | None = Field(None, title="Car Model")
    car_number: str | None = Field(None, title="Car Number")
    car_class: CarClass | None = Field(None, title="Car Class")
    car_status: CarStatus | None = Field(None, title="Car Status")
    driver_id: int | None = Field(None, title="Driver ID")

class CarSchemaNoDriver(BaseCarSchema):
    id: int = Field(..., title="Car ID")
    created_at: datetime = Field(..., title="Creation Timestamp")

class CarSchema(BaseCarSchema):
    id: int = Field(..., title="Car ID")
    driver: UserSchema | None = Field(None, title="Driver Information")
    created_at: datetime = Field(..., title="Creation Timestamp")