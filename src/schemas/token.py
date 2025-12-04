from pydantic import BaseModel
from src.enums.roles import UserRole

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    
class TokenDataSchema(BaseModel):
    user_id: str
    role: UserRole