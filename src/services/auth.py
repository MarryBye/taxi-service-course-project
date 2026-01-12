from src.controllers.database import DatabaseController
from src.schemas.auth import LoginSchema, RegisterSchema, TokenDataSchema, AuthenticateResponse
from src.schemas.views import UsersView


class AuthService:
    @staticmethod
    def authenticate(data: LoginSchema) -> Exception | AuthenticateResponse:
        db = DatabaseController()
        db.connect()

        query = "SELECT * FROM public.authenticate(%s, %s)"
        params = [data.login, data.password]

        return db.execute(query, params=params, fetch_count=1)

    @staticmethod
    def register(data: RegisterSchema) -> Exception | UsersView:
        db = DatabaseController()
        db.connect()

        query = "SELECT * FROM public.register(%s, %s, %s, %s, %s, %s, %s)"
        params = [
            data.login,
            data.password,
            data.first_name,
            data.last_name,
            data.email,
            data.tel_number,
            data.city_id
        ]

        return db.execute(query, params=params, fetch_count=1)

    @staticmethod
    def logout(user: TokenDataSchema = None) -> Exception | None:
        db = DatabaseController()
        try:
            db.disconnect(username=user.login)
        except Exception as e:
            return e