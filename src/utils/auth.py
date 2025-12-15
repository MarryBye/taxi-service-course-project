from fastapi import HTTPException, status, Request, Response, Header
from src.schemas.token import TokenDataSchema
from src.utils.crypto import CryptoUtil

class Auth:
    @staticmethod
    def verify_user(req: Request, token: str = Header(...)) -> TokenDataSchema | None:
        try:
            payload = CryptoUtil.verify_access_token(token)
            return TokenDataSchema(
                id=payload.id,
                login=payload.login,
                password=payload.password,
                role=payload.role
            )
        except Exception as e:
            return None


