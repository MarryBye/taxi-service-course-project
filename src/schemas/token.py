from pydantic import BaseModel, Field
from src.enums.roles import UserRole

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    
class TokenDataSchema(BaseModel):
    login: str = Field(..., alias="login", description="User's login")
    password: str = Field(..., alias="password", description="User's password")