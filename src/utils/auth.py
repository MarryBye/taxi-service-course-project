from fastapi import HTTPException, status, Header
from src.utils.crypto import CryptoUtil
from src.schemas.token import TokenDataSchema

class Auth:
    @staticmethod
    def verify_token(token: str = Header(...)) -> TokenDataSchema | None:
        payload = CryptoUtil.verify_access_token(token)
        if not payload:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
        return payload