from src.controllers.database import database
from src.schemas.profile import UpdateProfileSchema
from src.enums.roles import UserRole


class ProfileService:
    @staticmethod
    def get(id: int, role: str = None):
        query = "SELECT * FROM get_profile(%s)"
        return database.execute(query, params=[id], fetch_count=1, role=role)

    @staticmethod
    def update(id: int, schema: UpdateProfileSchema, role: UserRole = None):
        query = "SELECT * FROM update_profile(%s, %s, %s, %s, %s)"
        params = [
            id,
            schema.email,
            schema.tel_number,
            schema.password,
            schema.first_name,
            schema.last_name,
            schema.role,
            schema.city_name,
            schema.country_name
        ]
        return database.execute(query, params=params, fetch_count=1, role=role)

    @staticmethod
    def delete(id: int, role: UserRole = None):
        query = "SELECT * FROM delete_profile(%s)"
        return database.execute(query, params=[id], fetch_count=0, role=role)