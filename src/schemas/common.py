from pydantic import BaseModel, Field
from src.enums.db import BalanceTypes, TransactionType, PaymentMethods

class Country(BaseModel):
    id: int = Field(...)
    code: str = Field(..., max_length=2)
    full_name: str = Field(..., max_length=32)

class City(BaseModel):
    id: int = Field(...)
    country: Country = Field(...)
    name: str = Field(..., max_length=32)

class Address(BaseModel):
    country: str = Field(..., max_length=32)
    city: str = Field(..., max_length=32)
    street: str = Field(..., max_length=64)
    house: str = Field(..., max_length=16)

class Transaction(BaseModel):
    id: int = Field(...)
    balance_type: BalanceTypes = Field(...)
    transaction_type: TransactionType = Field(...)
    payment_method: PaymentMethods = Field(...)
    amount: int = Field(...)
    created_at: str = Field(...)

class Route(BaseModel):
    id: int = Field(...)
    start_location: Address = Field(...)
    end_location: Address = Field(...)
    distance: float = Field(...)
    all_addresses: list[Address] = Field(...)

class Rating(BaseModel):
    id: int = Field(...)
    mark: int = Field(...)
    created_at: str = Field(...)

class Cancel(BaseModel):
    id: int = Field(...)
    canceled_by: int = Field(...)
    comment: str = Field(...)
    created_at: str = Field(...)