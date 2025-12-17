from pydantic import BaseModel, Field
from src.enums.db import UserRole

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    
class TokenDataSchema(BaseModel):
    id: int = Field(..., alias="id", description="User ID")
    login: str = Field(..., alias="login", description="User's login")
    role: UserRole = Field(..., alias="role", description="User's role", max_length=32)