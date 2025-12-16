from fastapi import HTTPException, status, Request
from src.schemas.token import TokenDataSchema
from src.services.public_service import PublicService


class PublicController:
    @staticmethod
    def current_user(
        req: Request,
        current_user: TokenDataSchema
    ):
        result = PublicService.get_current_user(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Current user not found")

        return result
