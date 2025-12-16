from src.controllers.database import Database
from src.schemas.auth import AuthUserSchema, RegisterUserSchema
from src.schemas.token import TokenDataSchema


class PublicService:
    @staticmethod
    def get_current_user(user: TokenDataSchema = None) -> Exception | dict:
        db = Database(user=user)
        query = "SELECT * FROM public.get_current_user()"
        return db.execute(query, fetch_count=1)