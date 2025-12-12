from pydantic import BaseModel, Field
from datetime import datetime
from src.enums.roles import UserRole
from src.enums.city_names import CityNames
from src.enums.country_names import CountryNames
from src.schemas.mixins.WithHashablePassword import WithHashablePassword


class BaseUserSchema(BaseModel):
    email: str = Field(..., alias="email", description="Email address of the user", max_length=128)
    tel_number: str = Field(..., alias="tel_number", description="Telephone number of the user", max_length=32)
    first_name: str = Field(..., alias="first_name", description="First name of the user", max_length=32)
    last_name: str = Field(..., alias="last_name", description="Last name of the user", max_length=32)
    country: CountryNames = Field(..., alias="country", description="Country of the user", max_length=32)
    city: CityNames = Field(..., alias="city", description="City of the user", max_length=32)
    role: UserRole = Field(..., alias="role", description="User's role", max_length=32)

class UserSchema(BaseUserSchema):
    id: int = Field(..., alias="id", description="User ID")
    payment_balance: int = Field(..., alias="payment_balance", description="Payment balance of the user")
    created_at: datetime = Field(..., alias="created_at", description="User created time")
    changed_at: datetime = Field(..., alias="changed_at", description="User updated time")

class CreateUserSchema(BaseModel, WithHashablePassword):
    login: str = Field(..., alias="login", description="User's login")
    password: str = Field(..., alias="password", description="User's password")
    email: str = Field(..., alias="email", description="Email address of the user", max_length=128)
    tel_number: str = Field(..., alias="tel_number", description="Telephone number of the user", max_length=32)
    first_name: str = Field(..., alias="first_name", description="First name of the user", max_length=32)
    last_name: str = Field(..., alias="last_name", description="Last name of the user", max_length=32)
    city_name: CityNames = Field(..., alias="city_name", description="City of the user", max_length=32)
    country_name: CountryNames = Field(..., alias="country_name", description="Country of the user", max_length=32)
    role: UserRole = Field(..., alias="role", description="User's role", max_length=32)

class UpdateUserSchema(BaseModel, WithHashablePassword):
    tel_number: str | None = Field(None, alias="tel_number", description="Telephone number of the user")
    password: str | None = Field(None, alias="password", description="User's password")
    email: str | None = Field(None, alias="email", description="Email address of the user", max_length=128)
    first_name: str | None = Field(None, alias="first_name", description="First name of the user", max_length=32)
    last_name: str | None = Field(None, alias="last_name", description="Last name of the user", max_length=32)
    city_name: CityNames | None = Field(None, alias="city", description="City of the user", max_length=32)
    country_name: CountryNames | None = Field(None, alias="country", description="Country of the user", max_length=32)
    role: UserRole  | None = Field(None, alias="role", description="User's role", max_length=32)
