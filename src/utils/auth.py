from fastapi import HTTPException, status, Request, Response, Header
from typing import Optional
from src.schemas.token import TokenDataSchema
from src.utils.crypto import CryptoUtil

class Auth:
    @staticmethod
    def verify_user(
        req: Request,
        token: Optional[str] = Header(None)
    ) -> Optional[TokenDataSchema]:
        if not token:
            return None

        try:
            payload = CryptoUtil.verify_access_token(token)
            return TokenDataSchema(
                id=payload.id,
                login=payload.login,
                password=payload.password,
                role=payload.role
            )
        except Exception:
            return None


