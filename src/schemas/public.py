from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CurrentUserSchema(BaseModel):
    id: int = Field(..., alias="id", description="User ID")