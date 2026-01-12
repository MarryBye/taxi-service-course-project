from pydantic import BaseModel, Field

from src.enums.db import DriverCancelTags, DriverTags, ClientTags

class CancelOrderSchema(BaseModel):
    comment: str = Field(...)
    tags: list[DriverCancelTags] = Field(...)

class RateOrderSchema(BaseModel):
    mark: int = Field(...)
    comment: str = Field(...)
    tags: list[ClientTags] = Field(...)

class WithdrawCashSchema(BaseModel):
    amount: int = Field(...)