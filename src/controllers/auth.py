from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.services.users_service import UsersService
from src.schemas.token import TokenSchema
from src.schemas.users import UserSchema, UserRegisterSchema, UserLoginSchema
from src.utils.auth import Auth, CryptoUtil
from src.enums.roles import UserRole

class AuthController:
    @staticmethod
    def login(schema: UserLoginSchema) -> TokenSchema:
        user = UsersService.auth(schema.login)

        if not user:
            raise HTTPException(401, "Wrong login")
        
        auth = CryptoUtil.verify_password(schema.password, user["password_hash"])
        if not auth:
            raise HTTPException(401, "Wrong password")

        token = CryptoUtil.create_access_token({"user_id": user["id"], 'role': user["role"]})
        return {"access_token": token, "token_type": "bearer"}
    
    @staticmethod
    def register(schema: UserRegisterSchema) -> UserSchema:
        schema.hash_password()
        user = UsersService.create(
            login=schema.login,
            email=schema.email,
            tel_number=schema.tel_number,
            password=schema.password,
            first_name=schema.first_name,
            last_name=schema.last_name,
            role=UserRole.CLIENT,
        )
        return user
    
    @staticmethod
    def logout() -> None:
        pass