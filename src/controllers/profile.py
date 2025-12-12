from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.services.profile_service import ProfileService
from src.schemas.profile import ProfileSchema, UpdateProfileSchema
from src.schemas.token import TokenDataSchema


class ProfileController:
    @staticmethod
    def detail_view(current_user: TokenDataSchema) -> ProfileSchema:
        user = ProfileService.get(current_user.id, current_user.role)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    @staticmethod
    def update_view(schema: UpdateProfileSchema, current_user: TokenDataSchema) -> ProfileSchema:
        user = ProfileService.update(current_user.user_id, schema, current_user.role)
        return user

    @staticmethod
    def delete_view(current_user: TokenDataSchema) -> JSONResponse:
        ProfileService.delete(current_user.user_id, current_user.role)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User deleted successfully"})