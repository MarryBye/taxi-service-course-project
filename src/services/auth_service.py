from src.controllers.database import database
from src.schemas.auth import RegisterUserSchema, AuthUserSchema


class AuthService:
    @staticmethod
    def login(schema: AuthUserSchema):
        try:
            database.connect(executor_data=schema)
        except Exception as e:
            return None
        return True

    @staticmethod
    def register(schema: RegisterUserSchema):
        query = "SELECT * FROM register_user(%s, %s, %s, %s, %s, %s, %s, %s)"
        params = [
            schema.login,
            schema.email,
            schema.tel_number,
            schema.password,
            schema.city_name,
            schema.country_name,
            schema.first_name,
            schema.last_name
        ]
        return database.execute(query, params=params, fetch_count=1)