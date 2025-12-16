from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse
from src.services.users_service import UsersService
from src.schemas.users import AdminCreateUserSchema, AdminUpdateUserSchema, UserSchema
from src.schemas.token import TokenDataSchema


class UsersController:
    @staticmethod
    def list(
            req: Request,
            current_user: TokenDataSchema
    ) -> list[UserSchema]:
        result = UsersService.list(user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error getting users")

        return result
    
    @staticmethod
    def detail(
            req: Request,
            user_id: int,
            current_user: TokenDataSchema
    ) -> UserSchema:
        result = UsersService.get(user_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        return result
    
    @staticmethod
    def create(
            req: Request,
            schema: AdminCreateUserSchema,
            current_user: TokenDataSchema
    ) -> JSONResponse:
        schema.hash_password()
        result = UsersService.create(schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))

        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User created successfully"})
    
    @staticmethod
    def update(
            req: Request,
            user_id: int,
            schema: AdminUpdateUserSchema,
            current_user: TokenDataSchema
    ) -> JSONResponse:
        schema.hash_password()
        result = UsersService.update(user_id, schema, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))

        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User updated successfully"})
    
    @staticmethod
    def delete(
            req: Request,
            user_id: int,
            current_user: TokenDataSchema
    ) -> JSONResponse:
        result = UsersService.delete(user_id, user=current_user)

        if isinstance(result, Exception):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))

        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User deleted successfully"})