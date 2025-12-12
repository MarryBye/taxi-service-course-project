from pydantic import BaseModel, Field
from src.enums.roles import UserRole
from src.enums.city_names import CityNames
from src.enums.country_names import CountryNames
from src.schemas.users import BaseUserSchema
from src.schemas.mixins.WithHashablePassword import WithHashablePassword

class AuthUserSchema(BaseModel):
    login: str = Field(..., alias="login", description="User's login")
    password: str = Field(..., alias="password", description="User's password")

class RegisterUserSchema(BaseModel, WithHashablePassword):
    login: str = Field(..., alias="login", description="User's login")
    email: str = Field(..., alias="email", description="Email address of the user", max_length=128)
    tel_number: str = Field(..., alias="tel_number", description="Telephone number of the user", max_length=32)
    password: str = Field(..., alias="password", description="User's password")
    city_name: CityNames = Field(..., alias="city", description="City of the user", max_length=32)
    country_name: CountryNames = Field(..., alias="country", description="Country of the user", max_length=32)
    first_name: str = Field(..., alias="first_name", description="First name of the user", max_length=32)
    last_name: str = Field(..., alias="last_name", description="Last name of the user", max_length=32)