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
    id: int
    link_id: str
    account_id: Optional[str]
    amount: float
    currency: str
    collected_at: datetime
    status: Optional[str]
    type: Optional[str]

    class Config:
        from_attributes = True 
