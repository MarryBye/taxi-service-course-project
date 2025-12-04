from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.services.users_service import UsersService
from src.schemas.users import UserSchema, UserCreateSchema, UserUpdateSchema
from src.schemas.token import TokenDataSchema

class UsersController:
    @staticmethod
    def list_view(current_user: TokenDataSchema) -> list[UserSchema]:
        users = UsersService.list()
        return users
    
    @staticmethod
    def detail_view(user_id: int, current_user: TokenDataSchema) -> UserSchema:
        user = UsersService.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    
    @staticmethod
    def create_view(schema: UserCreateSchema, current_user: TokenDataSchema) -> UserSchema:
        schema.hash_password()
        user = UsersService.create(
            login=schema.login,
            email=schema.email,
            tel_number=schema.tel_number,
            password=schema.password,
            first_name=schema.first_name,
            last_name=schema.last_name,
            role=schema.role
        )
        return user
    
    @staticmethod
    def update_view(user_id: int, schema: UserUpdateSchema, current_user: TokenDataSchema) -> UserSchema:
        schema.hash_password()
        user = UsersService.update(
            id=user_id,
            email=schema.email,
            tel_number=schema.tel_number,
            password=schema.password,
            first_name=schema.first_name,
            last_name=schema.last_name,
            role=schema.role
        )
        return user
    
    @staticmethod
    def delete_view(user_id: int, current_user: TokenDataSchema) -> None:
        UsersService.delete(user_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User deleted successfully"})