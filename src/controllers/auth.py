from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse
from src.services.auth_service import AuthService
from src.schemas.token import TokenSchema, TokenDataSchema
from src.schemas.auth import AuthUserSchema, RegisterUserSchema
from src.utils.crypto import CryptoUtil

class AuthController:
    @staticmethod
    def login(
            req: Request,
            schema: AuthUserSchema,
            current_user: AuthUserSchema
    ) -> TokenSchema:
        result = AuthService.login(schema)

        if not result:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

        token = CryptoUtil.create_access_token(TokenDataSchema(login=schema.login, password=schema.password))
        req.session["TOKEN"] = token

        result = TokenSchema(access_token=token, token_type="bearer")

        return result
    
    @staticmethod
    def register(
            req: Request,
            schema: RegisterUserSchema,
            current_user: AuthUserSchema
    ) -> JSONResponse:
        user = AuthService.register(schema)

        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

        return JSONResponse("Successfully signed up!", status_code=status.HTTP_200_OK)
    
    @staticmethod
    def logout(
        req: Request,
        current_user: AuthUserSchema
    ) -> JSONResponse:
        # req.session.clear()

        print(current_user)

        return JSONResponse("Successfully signed out!", status_code=status.HTTP_200_OK)