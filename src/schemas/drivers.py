from pydantic import BaseModel, Field
from src.schemas.cars import CarSchemaNoDriver
from src.schemas.users import UserSchema

class DriverSchema(UserSchema):
    car: CarSchemaNoDriver | None = Field(None, title="Assigned Car Information")