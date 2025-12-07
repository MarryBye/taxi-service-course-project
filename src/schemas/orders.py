from pydantic import BaseModel, Field
from datetime import datetime
from src.schemas.users import UserSchema
from src.enums.order_statuses import OrderStatuses

class BaseOrderSchema(BaseModel):
    status: OrderStatuses = Field(..., title="Order Status")
    client: UserSchema = Field(..., title="Client Information")
    driver: UserSchema | None = Field(None, title="Driver Information")
    created_at: datetime = Field(..., title="Order Creation Timestamp")
    finished_at: datetime | None = Field(None, title="Order Completion Timestamp")
    
class OrderCreateSchema(BaseModel):
    client_id: int = Field(..., title="Client ID")
    
class OrderUpdateSchema(BaseModel):
    status: OrderStatuses | None = Field(None, title="Order Status")
    driver_id: int | None = Field(None, title="Driver ID")
    finished_at: datetime | None = Field(None, title="Order Completion Timestamp")
    
class OrderSchema(BaseOrderSchema):
    id: int = Field(..., title="Order ID")
    client_rating: int | None = Field(None, title="Client Rating")
    client_comment: str | None = Field(None, title="Client Comment", max_length=512)
    client_rating_created_at: datetime | None = Field(None, title="Client Rating Creation Timestamp")
    driver_rating: int | None = Field(None, title="Driver Rating")
    driver_comment: str | None = Field(None, title="Driver Comment", max_length=512)
    driver_rating_created_at: datetime | None = Field(None, title="Driver Rating Creation Timestamp")
    order_canceled_by: int | None = Field(None, title="ID of User Who Canceled the Order")
    order_cancel_comment: str | None = Field(None, title="Order Cancellation Comment", max_length=512)