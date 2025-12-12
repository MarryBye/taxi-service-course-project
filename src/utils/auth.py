from fastapi import HTTPException, status, Request, Response
from src.schemas.token import TokenDataSchema
from src.utils.crypto import CryptoUtil

class Auth:
    @staticmethod
    def verify_user(req: Request) -> TokenDataSchema | None:
        try:
            payload = CryptoUtil.verify_access_token(req.session.get("TOKEN"))
            return TokenDataSchema(
                id=payload.id,
                login=payload.login,
                password=payload.password,
                role=payload.role
            )
        except Exception as e:
            req.session.clear()
            return None


