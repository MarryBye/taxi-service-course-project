from pydantic import BaseModel, Field
from datetime import datetime
from src.enums.roles import UserRole
from src.utils.crypto import CryptoUtil

class UserPasswordSchema:    
    def hash_password(self) -> None:
        self.password = CryptoUtil.hash_password(self.password)

class BaseUserSchema(BaseModel):
    first_name: str = Field(..., title="First Name", max_length=32)
    last_name: str = Field(..., title="Last Name", max_length=32)
    email: str = Field(..., title="Email Address", max_length=128)
    tel_number: str = Field(..., title="Telephone Number", max_length=32)
    role: UserRole = Field(..., title="User Role")

class UserCreateSchema(BaseUserSchema, UserPasswordSchema):
    login: str = Field(..., max_length=32)
    password: str = Field(..., title="Password", max_length=512)
    
class UserUpdateSchema(BaseModel, UserPasswordSchema):
    first_name: str | None = Field(None, title="First Name", max_length=32)
    last_name: str | None = Field(None, title="Last Name", max_length=32)
    email: str | None = Field(None, title="Email Address", max_length=128)
    tel_number: str | None = Field(None, title="Telephone Number", max_length=32)
    password: str | None = Field(None, title="Password", max_length=512)

class UserSchema(BaseUserSchema):
    id: int = Field(..., title="User ID")
    created_at: datetime = Field(..., title="Creation Timestamp")

class UserLoginSchema(BaseModel, UserPasswordSchema):
    login: str = Field(..., max_length=32)
    password: str = Field(..., title="Password", max_length=512)
    
class UserRegisterSchema(BaseModel, UserPasswordSchema):
    login: str = Field(..., title="Login", max_length=32)
    password: str = Field(..., title="Password", max_length=512)
    first_name: str | None = Field(None, title="First Name", max_length=32)
    last_name: str | None = Field(None, title="Last Name", max_length=32)
    email: str | None = Field(None, title="Email Address", max_length=128)
    tel_number: str | None = Field(None, title="Telephone Number", max_length=32)
    
class UserAuthSchema(UserPasswordSchema):
    login: str = Field(..., title="Login", max_length=32)
    password: str = Field(..., title="Password", max_length=512)
    role: UserRole = Field(..., title="User Role")