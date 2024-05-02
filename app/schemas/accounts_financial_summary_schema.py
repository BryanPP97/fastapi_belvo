from pydantic import BaseModel
from typing import List

class AccountSummary(BaseModel):
    account_id: str
    total_inflow: float
    total_outflow: float

class AccountsFinancialSummary(BaseModel):
    accounts: List[AccountSummary]
