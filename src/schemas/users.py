from pydantic import BaseModel, Field
from datetime import datetime
from src.enums.roles import UserRole

class BaseUserSchema(BaseModel):
    first_name: str = Field(..., title="First Name", max_length=32)
    last_name: str = Field(..., title="Last Name", max_length=32)
    email: str = Field(..., title="Email Address", max_length=128)
    tel_number: str = Field(..., title="Telephone Number", max_length=32)
    role: UserRole = Field(..., title="User Role")

class UserUpdateSchema(BaseModel):
    first_name: str | None = Field(None, title="First Name", max_length=32)
    last_name: str | None = Field(None, title="Last Name", max_length=32)
    email: str | None = Field(None, title="Email Address", max_length=128)
    tel_number: str | None = Field(None, title="Telephone Number", max_length=32)
    password_hash: str | None = Field(None, title="Password Hash", max_length=128)
    role: UserRole | None = Field(None, title="User Role")     
    
    def hash_password(self):
        if self.password_hash:
            self.password_hash = "hashed_" + self.password_hash

class UserCreateSchema(BaseUserSchema):
    login: str = Field(..., title="Login", max_length=32)
    password_hash: str = Field(..., title="Password Hash", max_length=128)
    
    def hash_password(self):
        self.password_hash = "hashed_" + self.password_hash
        
class UserSchema(BaseUserSchema):
    id: int = Field(..., title="User ID")
    created_at: datetime = Field(..., title="Creation Timestamp")