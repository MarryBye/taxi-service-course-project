from src.controllers.database import Database
from src.schemas.auth import AuthUserSchema, RegisterUserSchema
from src.schemas.token import TokenDataSchema


class AuthService:
    @staticmethod
    def auth(data: AuthUserSchema, user: TokenDataSchema = None) -> Exception | dict:
        db = Database(user=user)

        query = "SELECT * FROM auth(%s)"
        params = [data.login]

        return db.execute(query, params=params, fetch_count=1)

    @staticmethod
    def register(schema: RegisterUserSchema, user: TokenDataSchema = None) -> Exception | dict:
        db = Database(user=user)

        query = "CALL register(%s, %s, %s, %s, %s, %s, %s, %s)"
        params = [
            schema.login,
            schema.email,
            schema.tel_number,
            schema.password,
            schema.first_name,
            schema.last_name,
            schema.country_name,
            schema.city_name
        ]

        return db.execute(query, params=params, fetch_count=0)