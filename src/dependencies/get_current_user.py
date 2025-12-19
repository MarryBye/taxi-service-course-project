from fastapi import Header
from typing import Optional
from src.schemas.auth import TokenDataSchema
from src.utils.crypto import CryptoUtil

def get_current_user(
        token: Optional[str] = Header(None)
) -> Optional[TokenDataSchema]:
    if not token:
        return None
    try:
        payload = CryptoUtil.verify_access_token(token)
        return TokenDataSchema(
            id=payload.id,
            login=payload.login,
            role=payload.role
        )
    except Exception as e:
        return None
