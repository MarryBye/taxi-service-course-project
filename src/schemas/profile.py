from pydantic import BaseModel, Field
from datetime import datetime
from src.enums.roles import UserRole
from src.enums.city_names import CityNames
from src.enums.country_names import CountryNames

class BaseProfileSchema(BaseModel):
    email: str = Field(..., alias="email", description="Email address of the user", max_length=128)
    tel_number: str = Field(..., alias="tel_number", description="Telephone number of the user", max_length=32)
    first_name: str = Field(..., alias="first_name", description="First name of the user", max_length=32)
    last_name: str = Field(..., alias="last_name", description="Last name of the user", max_length=32)
    country: CountryNames = Field(..., alias="country", description="Country of the user", max_length=32)
    city: CityNames = Field(..., alias="city", description="City of the user", max_length=32)
    role: UserRole = Field(..., alias="role", description="User's role", max_length=32)

class ProfileSchema(BaseProfileSchema):
    id: int = Field(..., alias="id", description="User ID")
    payment_balance: int = Field(..., alias="payment_balance", description="Payment balance of the user")
    created_at: datetime = Field(..., alias="created_at", description="User created time")
    changed_at: datetime = Field(..., alias="changed_at", description="User updated time")

class UpdateProfileSchema(BaseModel):
    first_name: str = Field(..., alias="first_name", description="First name of the user", max_length=32)
    last_name: str = Field(..., alias="last_name", description="Last name of the user", max_length=32)
    country: CountryNames = Field(..., alias="country", description="Country of the user", max_length=32)
    city: CityNames = Field(..., alias="city", description="City of the user", max_length=32)