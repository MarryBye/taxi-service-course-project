from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.services.staff_service import StaffService
from src.schemas.drivers import StaffSchema, StaffCreateSchema, StaffUpdateSchema
from src.schemas.token import TokenDataSchema


class StaffController:
    @staticmethod
    def list_view(current_user: TokenDataSchema) -> list[StaffSchema]:
        users = StaffService.list()
        return users

    @staticmethod
    def detail_view(user_id: int, current_user: TokenDataSchema) -> StaffSchema:
        user = StaffService.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    @staticmethod
    def create_view(schema: StaffCreateSchema, current_user: TokenDataSchema) -> StaffSchema:
        schema.hash_password()
        user = StaffService.create(
            login=schema.login,
            email=schema.email,
            tel_number=schema.tel_number,
            password=schema.password,
            first_name=schema.first_name,
            last_name=schema.last_name
        )
        return user

    @staticmethod
    def update_view(user_id: int, schema: StaffUpdateSchema, current_user: TokenDataSchema) -> StaffSchema:
        schema.hash_password()
        user = StaffService.update(
            id=user_id,
            email=schema.email,
            tel_number=schema.tel_number,
            password=schema.password,
            first_name=schema.first_name,
            last_name=schema.last_name
        )
        return user

    @staticmethod
    def delete_view(user_id: int, current_user: TokenDataSchema) -> None:
        StaffService.delete(user_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User deleted successfully"})