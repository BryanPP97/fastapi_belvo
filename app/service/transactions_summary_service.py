from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.transactions_schema import TransactionSummary
from app.models.transactions_models import Transaction
from app.api.dependencies import get_db
from app.api.dependencies import validate_token
from sqlalchemy import func



router = APIRouter()


@router.get("/transactions/summary-by-category/{link_id}", response_model=TransactionSummary)
def summary_by_category(link_id: str, db: Session = Depends(get_db), token: str = Depends(validate_token)):

    try:
        # Consulta que suma las transacciones por categoría filtrando por link_id y tipo de transacción
        results = db.query(
            Transaction.transaction_category,
            func.sum(Transaction.amount).label("total_amount")
        ).filter(
            Transaction.link_id == link_id,  # Filtra por link_id
            Transaction.transaction_type == 'OUTFLOW'  # Considera solo los egresos
        ).group_by(
            Transaction.transaction_category
        ).all()

        # Prepara el resumen de categorías a partir de los resultados
        category_totals = {transaction_category: total for transaction_category, total in results}
        return {"totals_by_category": category_totals}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error summarizing transactions by category: {str(e)}")