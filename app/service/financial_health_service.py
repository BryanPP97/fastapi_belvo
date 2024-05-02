from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.transactions_models import Transaction # Asegúrate de tener importada la definición correcta
from app.schemas.financial_health_schema import FinancialHealthSummary  # Importa tu schema de Pydantic
from app.api.dependencies import validate_token
from sqlalchemy import func
from app.api.dependencies import get_db

router = APIRouter()

@router.get("/transactions/financial-health/{link_id}", response_model=FinancialHealthSummary)
def financial_health(link_id: str, db: Session = Depends(get_db), token: str = Depends(validate_token)):
    
    # Calcular ingresos totales solo para el link_id proporcionado
    total_inflow = db.query(func.sum(Transaction.amount))\
                     .filter(
                         Transaction.link_id == link_id,
                         Transaction.transaction_type == 'INFLOW'
                     )\
                     .scalar() or 0

    # Calcular egresos totales solo para el link_id proporcionado
    total_outflow = db.query(func.sum(Transaction.amount))\
                      .filter(
                          Transaction.link_id == link_id,
                          Transaction.transaction_type == 'OUTFLOW'
                      )\
                      .scalar() or 0

    # Determinar la salud financiera (ratio de ingresos a egresos)
    health_score = total_inflow / total_outflow if total_outflow > 0 else float('inf')  # Evita la división por cero

    return FinancialHealthSummary(
        total_inflow=total_inflow,
        total_outflow=total_outflow,
        financial_health_score=health_score
    )
