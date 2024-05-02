from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.api.dependencies import validate_token
from app.models.transactions_models import Transaction
from app.schemas.accounts_financial_summary_schema import AccountsFinancialSummary, AccountSummary
from sqlalchemy import func

router = APIRouter()

@router.get("/transactions/accounts-financial-summary/{link_id}", response_model=AccountsFinancialSummary)
def accounts_financial_summary(link_id: str, db: Session = Depends(get_db), token: str = Depends(validate_token)):
    try:
        # Filtrar transacciones por el link_id proporcionado y agruparlas por cuenta y tipo de transacción
        account_totals = db.query(
            Transaction.account_id,
            func.sum(Transaction.amount).label("total_amount"),
            Transaction.transaction_type
        ).filter(
            Transaction.link_id == link_id,  # Filtra por link_id
            Transaction.transaction_type.in_(['INFLOW', 'OUTFLOW'])  # Asegura que solo se consideren entradas y salidas válidas
        ).group_by(
            Transaction.account_id,
            Transaction.transaction_type
        ).all()

        # Estructurar los datos para el resumen
        accounts = {}
        for account_id, total_amount, transaction_type in account_totals:
            if account_id not in accounts:
                accounts[account_id] = {"total_inflow": 0, "total_outflow": 0}
            if transaction_type == 'INFLOW':
                accounts[account_id]["total_inflow"] += total_amount
            elif transaction_type == 'OUTFLOW':
                accounts[account_id]["total_outflow"] -= total_amount  #  outflows como negativos

        # Convertir el diccionario en la lista de AccountSummary
        summary_list = [AccountSummary(account_id=acc, total_inflow=info["total_inflow"], total_outflow=info["total_outflow"]) for acc, info in accounts.items()]

        return AccountsFinancialSummary(accounts=summary_list)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error summarizing transactions: {str(e)}")
