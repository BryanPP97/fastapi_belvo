from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.transactions_schema import TransactionResponse, TransactionFilter, TransactionSummary
from app.models.transactions_models import Transaction
from app.api.dependencies import get_db
from app.api.dependencies import validate_token
from sqlalchemy import func
from app.core.config import get_belvo_client
from dateutil import parser

router = APIRouter()

@router.get("/transactions", response_model=List[TransactionResponse])
def list_transactions(filters: TransactionFilter = Depends(), db: Session = Depends(get_db), token: str = Depends(validate_token)):
    try:
        belvo_client = get_belvo_client()
        transactions_data = belvo_client.Transactions.list(
            link=filters.link_id,
            date_from=filters.date_from,
            date_to=filters.date_to,
            page=filters.page,
            page_size=filters.page_size
        )

        transactions = []
        for txn in transactions_data:
            transaction = Transaction(
                transaction_id=txn['id'],
                account_id=txn['account']['id'],
                link_id=txn['account']['link'],
                account_name=txn['account']['name'],
                account_type=txn['account']['type'],
                transaction_category=txn['category'],
                transaction_type=txn['type'],
                amount=txn['amount'],
                status=txn.get('status','Unknown'),
                currency=txn['currency'],
                description=txn['description'],
            )
            transactions.append(transaction)



        db.bulk_save_objects(transactions)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error processing transactions: {str(e)}")

    return [TransactionResponse.from_orm(txn) for txn in transactions]







