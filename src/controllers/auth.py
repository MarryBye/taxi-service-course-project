from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse
from src.services.auth_service import AuthService
from src.schemas.token import TokenSchema, TokenDataSchema
from src.schemas.auth import AuthUserSchema, RegisterUserSchema, AuthResponseUserSchema
from src.utils.crypto import CryptoUtil

class AuthController:
    @staticmethod
    def login(
            req: Request,
            schema: AuthUserSchema,
            user: TokenDataSchema
    ) -> TokenSchema:
        result = AuthService.auth(schema, user)

        if isinstance(result, Exception):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))

        if not result:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username")

        result = AuthResponseUserSchema(
            id = result["id"],
            login = result["login"],
            password = result["password_hash"],
            role = result["role"]
        )

        if not CryptoUtil.verify_password(schema.password, result.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

        token = CryptoUtil.create_access_token(
            TokenDataSchema(
                id = result.id,
                login = result.login,
                password = result.password,
                role = result.role
            )
        )

        result = TokenSchema(access_token=token, token_type="bearer")

        return result
    
    @staticmethod
    def register(
            req: Request,
            schema: RegisterUserSchema,
            user: TokenDataSchema
    ) -> JSONResponse:
        schema.hash_password()
        user = AuthService.register(schema)

        if isinstance(user, Exception):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(user))

        return JSONResponse("Successfully signed up!", status_code=status.HTTP_200_OK)
    
    @staticmethod
    def logout(
        req: Request,
        user: TokenDataSchema
    ) -> JSONResponse:

        return JSONResponse("Successfully signed out!", status_code=status.HTTP_200_OK)