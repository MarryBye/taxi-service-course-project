from pydantic import BaseModel, Field
from src.enums.db import ClientCancelTags, ClientTags

class CancelOrderSchema(BaseModel):
    comment: str = Field(...)
    tags: list[ClientCancelTags] = Field(...)

class RateOrderSchema(BaseModel):
    mark: int = Field(...)
    comment: str = Field(...)
    tags: list[ClientTags]