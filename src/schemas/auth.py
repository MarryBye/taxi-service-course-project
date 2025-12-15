from pydantic import BaseModel, Field
from src.enums.db import UserRole, CountryName, CityName
from src.schemas.mixins.hashable_password import WithHashablePassword

class AuthUserSchema(BaseModel):
    login: str = Field(..., alias="login", description="User's login")
    password: str = Field(..., alias="password", description="User's password")

class AuthResponseUserSchema(BaseModel):
    id: int = Field(..., alias="id", description="User ID")
    login: str = Field(..., alias="login", description="User's login")
    password: str = Field(..., alias="password", description="User's password")
    role: UserRole = Field(..., alias="role", description="User's role", max_length=32)

class RegisterUserSchema(BaseModel, WithHashablePassword):
    login: str = Field(..., alias="login", description="User's login")
    email: str = Field(..., alias="email", description="Email address of the user", max_length=128)
    tel_number: str = Field(..., alias="tel_number", description="Telephone number of the user", max_length=32)
    password: str = Field(..., alias="password", description="User's password")
    first_name: str = Field(..., alias="first_name", description="First name of the user", max_length=32)
    last_name: str = Field(..., alias="last_name", description="Last name of the user", max_length=32)
    country_name: CountryName = Field(..., alias="country", description="Country of the user", max_length=32)
    city_name: CityName = Field(..., alias="city", description="City of the user", max_length=32)
