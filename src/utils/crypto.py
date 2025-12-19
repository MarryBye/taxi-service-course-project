from jose import JWTError, jwt
from datetime import datetime, timedelta
from config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_TOKEN_LIFETIME
from src.schemas.auth import TokenDataSchema

class CryptoUtil:
    @staticmethod
    def create_access_token(data: TokenDataSchema) -> str:
        to_encode = data.dict()
        expire = datetime.now() + timedelta(minutes=JWT_TOKEN_LIFETIME)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def verify_access_token(token: str) -> TokenDataSchema | None:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            return TokenDataSchema(**payload)
        except JWTError:
            return None