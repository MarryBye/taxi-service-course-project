from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import UserRole, CountryName, CityName
from src.schemas.mixins.hashable_password import WithHashablePassword


class BaseUserSchema(BaseModel):
    email: str = Field(..., alias="email", description="Email address of the user", max_length=128)
    tel_number: str = Field(..., alias="tel_number", description="Telephone number of the user", max_length=32)
    first_name: str = Field(..., alias="first_name", description="First name of the user", max_length=32)
    last_name: str = Field(..., alias="last_name", description="Last name of the user", max_length=32)
    country: CountryName = Field(..., alias="country", description="Country of the user", max_length=32)
    city: CityName = Field(..., alias="city", description="City of the user", max_length=32)
    role: UserRole = Field(..., alias="role", description="User's role", max_length=32)

class UserSchema(BaseUserSchema):
    id: int = Field(..., alias="id", description="User ID")
    created_at: datetime = Field(..., alias="created_at", description="User created time")
    changed_at: datetime = Field(..., alias="changed_at", description="User updated time")

class UpdateUserSchema(BaseModel, WithHashablePassword):
    tel_number: Optional[str] = Field(None, alias="tel_number", description="Telephone number of the user")
    password: Optional[str] = Field(None, alias="password", description="User's password")
    email: Optional[str] = Field(None, alias="email", description="Email address of the user", max_length=128)
    first_name: Optional[str] = Field(None, alias="first_name", description="First name of the user", max_length=32)
    last_name: Optional[str] = Field(None, alias="last_name", description="Last name of the user", max_length=32)
    city_name: Optional[CityName] = Field(None, alias="city", description="City of the user", max_length=32)
    country_name: Optional[CountryName] = Field(None, alias="country", description="Country of the user", max_length=32)

class AdminUpdateUserSchema(UpdateUserSchema):
    role: Optional[UserRole] = Field(None, alias="role", description="User's role", max_length=32)

class AdminCreateUserSchema(BaseUserSchema, WithHashablePassword):
    login: str = Field(..., alias="login", description="User's login")
    password: str = Field(..., alias="password", description="User's password")