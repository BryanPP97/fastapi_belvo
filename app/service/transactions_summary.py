from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.transactions_schema import TransactionSummary
from app.models.transactions_models import Transaction
from app.api.dependencies import get_db
from app.api.dependencies import validate_token
from sqlalchemy import func



router = APIRouter()


@router.get("/transactions/summary-by-category", response_model=TransactionSummary)
def summary_by_category(db: Session = Depends(get_db), token: str = Depends(validate_token)):
    
    results = db.query(
        Transaction.transaction_category,
        func.sum(Transaction.amount).label("total_amount")
    ).filter(
        Transaction.transaction_type == 'OUTFLOW'
    ).group_by(
        Transaction.transaction_category
    ).all()

    category_totals = {transaction_category: total for transaction_category, total in results}
    return {"totals_by_category": category_totals}