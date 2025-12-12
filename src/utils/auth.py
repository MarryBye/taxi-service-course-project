from fastapi import HTTPException, status, Request, Response
from src.schemas.auth import AuthUserSchema
from src.utils.crypto import CryptoUtil

class Auth:
    @staticmethod
    def verify_user(req: Request) -> AuthUserSchema | None:
        try:
            payload = CryptoUtil.verify_access_token(req.session.get("TOKEN"))
            return AuthUserSchema(login=payload.login, password=payload.password)
        except Exception as e:
            req.session.clear()
            return None


