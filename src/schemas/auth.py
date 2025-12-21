from pydantic import BaseModel, Field
from src.enums.db import UserRoles

class LoginSchema(BaseModel):
    login: str = Field(...)
    password: str = Field(...)

class RegisterSchema(BaseModel):
    login: str = Field(..., max_length=32)
    password: str = Field(..., max_length=32)
    first_name: str = Field(..., max_length=32)
    last_name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=32)
    tel_number: str = Field(..., max_length=32)
    city_id: int = Field(...)

class AuthenticateResponse(BaseModel):
    id: int = Field(...)
    role: UserRoles = Field(...)

class TokenSchema(BaseModel):
    token_type: str = Field(...)
    access_token: str = Field(...)

class TokenDataSchema(BaseModel):
    id: int = Field(...)
    login: str = Field(...)
    role: UserRoles = Field(...)