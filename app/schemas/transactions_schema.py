from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional, List

class TransactionFilter(BaseModel):
    link_id: str
    account_id: Optional[str] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    currency: Optional[str] = None
    page: Optional[int] = 1
    page_size: Optional[int] = 100

class TransactionResponse(BaseModel):
    transaction_id: str
    link_id: str
    account_id: Optional[str]
    account_name: str
    account_type: str
    transaction_category: Optional[str]
    transaction_type: str
    amount: float
    status: Optional[str]
    currency: str
    description: str

    
    class Config:
        from_attributes = True

class Transaction(BaseModel):
    id: str
    transaction_category: str
    amount: float
    currency: str

class TransactionsPage(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Transaction]

class TransactionSummary(BaseModel):
    totals_by_category: dict
