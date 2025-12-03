from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.services.users_service import UsersService
from src.schemas.users import UserSchema, UserCreateSchema, UserUpdateSchema

class UsersController:
    @staticmethod
    async def list_view() -> list[UserSchema]:
        users = UsersService.list()
        return users
    
    @staticmethod
    async def detail_view(user_id: int) -> UserSchema:
        user = UsersService.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    
    @staticmethod
    async def create_view(schema: UserCreateSchema) -> UserSchema:
        schema.hash_password()
        user = UsersService.create(
            login=schema.login,
            email=schema.email,
            tel_number=schema.tel_number,
            password_hash=schema.password_hash,
            first_name=schema.first_name,
            last_name=schema.last_name,
            role=schema.role
        )
        return user
    
    @staticmethod
    async def update_view(user_id: int, schema: UserUpdateSchema) -> UserSchema:
        schema.hash_password()
        user = UsersService.update(
            id=user_id,
            email=schema.email,
            tel_number=schema.tel_number,
            password_hash=schema.password_hash,
            first_name=schema.first_name,
            last_name=schema.last_name,
            role=schema.role
        )
        return user
    
    @staticmethod
    async def delete_view(user_id: int) -> None:
        UsersService.delete(user_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User deleted successfully"})