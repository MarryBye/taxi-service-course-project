from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.services.drivers_service import DriversService
from src.schemas.drivers import DriverSchema, DriverCreateSchema, DriverUpdateSchema
from src.schemas.token import TokenDataSchema


class DriversController:
    @staticmethod
    def list_view(current_user: TokenDataSchema) -> list[DriverSchema]:
        users = DriversService.list()
        return users

    @staticmethod
    def detail_view(user_id: int, current_user: TokenDataSchema) -> DriverSchema:
        user = DriversService.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    @staticmethod
    def create_view(schema: DriverCreateSchema, current_user: TokenDataSchema) -> DriverSchema:
        schema.hash_password()
        user = DriversService.create(
            login=schema.login,
            email=schema.email,
            tel_number=schema.tel_number,
            password=schema.password,
            first_name=schema.first_name,
            last_name=schema.last_name
        )
        return user

    @staticmethod
    def update_view(user_id: int, schema: DriverUpdateSchema, current_user: TokenDataSchema) -> DriverSchema:
        schema.hash_password()
        user = DriversService.update(
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
        DriversService.delete(user_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User deleted successfully"})