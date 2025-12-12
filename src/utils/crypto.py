from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_TOKEN_LIFETIME
from src.schemas.token import TokenDataSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
            payload = TokenDataSchema(**jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]))
            return payload
        except JWTError:
            return None
        
    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)