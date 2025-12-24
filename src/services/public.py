from src.controllers.database import DatabaseController
from src.schemas.auth import TokenDataSchema
from src.schemas.views import *
from src.schemas.common import *


class PublicService:
    @staticmethod
    def get_countries() -> Exception | list[Country]:
        db = DatabaseController()

        query = """
            SELECT * FROM public.get_countries()
        """
        params = []

        return db.execute(query, params=params, fetch_count=-1)

    @staticmethod
    def get_cities(country_id: int) -> Exception | list[City]:
        db = DatabaseController()

        query = """
            SELECT * FROM public.get_cities(%s)
        """
        params = [country_id]

        return db.execute(query, params=params, fetch_count=-1)