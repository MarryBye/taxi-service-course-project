from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse
from src.services.users_service import UsersService
from src.schemas.users import UserSchema, CreateUserSchema, UpdateUserSchema
from src.schemas.auth import AuthUserSchema
from src.schemas.token import TokenDataSchema

class UsersController:
    @staticmethod
    def list_view(
            req: Request,
            current_user: AuthUserSchema
    ) -> list[UserSchema]:
        users = UsersService.list(executor=current_user)

        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error getting users")

        return users
    
    @staticmethod
    def detail_view(
            req: Request,
            user_id: int,
            current_user: AuthUserSchema
    ) -> UserSchema:
        user = UsersService.get(user_id, executor=current_user)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    
    @staticmethod
    def create_view(
            req: Request,
            schema: CreateUserSchema,
            current_user: AuthUserSchema
    ) -> UserSchema:
        # schema.hash_password()
        user = UsersService.create(schema, executor=current_user)
        return user
    
    @staticmethod
    def update_view(
            req: Request,
            user_id: int,
            schema: UpdateUserSchema,
            current_user: AuthUserSchema
    ) -> UserSchema:
        # schema.hash_password()
        user = UsersService.update(user_id, schema, executor=current_user)
        return user
    
    @staticmethod
    def delete_view(
            user_id: int,
            current_user: AuthUserSchema
    ) -> JSONResponse:
        UsersService.delete(user_id, executor=current_user)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User deleted successfully"})