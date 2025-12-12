from pydantic import BaseModel, Field
from src.enums.roles import UserRole

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    
class TokenDataSchema(BaseModel):
    id: int = Field(..., alias="id", description="User ID")
    login: str = Field(..., alias="login", description="User's login")
    password: str = Field(..., alias="password", description="User's password")
    role: UserRole = Field(..., alias="role", description="User's role", max_length=32)