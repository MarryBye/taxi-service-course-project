from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import UserRole

class CurrentUserSchema(BaseModel):
    id: Optional[int] = Field(None, alias="id", description="User ID")
    role: UserRole = Field(..., alias="role", description="User's role")