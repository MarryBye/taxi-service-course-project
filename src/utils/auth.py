from fastapi import HTTPException, status, Header
from src.utils.crypto import CryptoUtil

class Auth:
    @staticmethod
    def verify_token(token: str = Header(...)) -> dict | None:
        payload = CryptoUtil.verify_access_token(token)
        if not payload:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
        return payload