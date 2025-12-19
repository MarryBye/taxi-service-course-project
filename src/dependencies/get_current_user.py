from fastapi import Header, HTTPException
from typing import Optional
from src.schemas.auth import TokenDataSchema
from src.utils.crypto import CryptoUtil

def get_current_user(
        token: Optional[str] = Header(None)
) -> Optional[TokenDataSchema]:
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = CryptoUtil.verify_access_token(token)
        return TokenDataSchema(
            id=payload.id,
            login=payload.login,
            role=payload.role
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
