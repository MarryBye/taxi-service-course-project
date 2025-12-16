from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import TransactionType, PaymentMethod, CarClass, BalanceType
from src.schemas.common import AddressSchema
from src.schemas.mixins.hashable_password import WithHashablePassword
from src.schemas.users import *

class BaseTransactionSchema(BaseModel):
    amount: int = Field(..., alias="amount", description="Transaction's amount")
    transaction_type: TransactionType = Field(..., alias="transaction_type", description="Transaction type")
    balance_type: BalanceType = Field(..., alias="balance_type", description="Balance type")
    user_id: int = Field(..., alias="user_id", description="User ID")
    payment_method: PaymentMethod = Field(..., alias="payment_method", description="Payment method")

class TransactionSchema(BaseTransactionSchema):
    id: int = Field(..., alias="id", description="Transaction ID")
    created_at: datetime = Field(..., alias="created_at", description="Transaction created time")

class CreateTransactionSchema(BaseTransactionSchema):
    user_id: int = Field(..., alias="user_id", description="User ID")
    balance_type: BalanceType = Field(..., alias="balance_type", description="Balance type")
    transaction_type: TransactionType = Field(..., alias="transaction_type", description="Transaction type")
    payment_method: PaymentMethod = Field(..., alias="payment_method", description="Payment method")
    amount: int = Field(..., alias="amount", description="Transaction's amount")