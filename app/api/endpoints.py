from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.core.auth import decode_access_token
from app.models.transactions_models import Transaction
from app.models.link_create import Link
from app.schemas.transactions_schema import TransactionFilter, TransactionResponse
from app.schemas.link_create import LinkCreate, LinkResponse
from app.api.dependencies import get_db
from app.core.config import get_belvo_client
from typing import List


router = APIRouter()

@router.get("/transactions", response_model=List[TransactionResponse])
def list_transactions(
    filters: TransactionFilter = Depends(),  
    db: Session = Depends(get_db),
    token: str = Depends(decode_access_token)
):
    if not token:
        raise HTTPException(status_code=401, detail="Token de acceso no proporcionado o no válido")
    
    try:
        belvo_client = get_belvo_client()
        # Llamada a la API de Belvo usando los filtros
        transactions_data = belvo_client.Transactions.list(
            link=filters.link_id,
            date_from=filters.date_from,
            date_to=filters.date_to,
            page=filters.page,
            page_size=filters.page_size
        )

        # Creación y almacenamiento de las transacciones en la base de datos
        transactions = [Transaction(
            link_id=txn['link'],
            account_id=txn.get('account_id', None),
            amount=txn['amount'],
            currency=txn['currency'],
            collected_at=txn['collected_at'],
            status=txn.get('status', None),
            type=txn.get('type', None)
        ) for txn in transactions_data]

        db.bulk_save_objects(transactions)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error processing transactions: {str(e)}")

    return [TransactionResponse.from_attributes(txn) for txn in transactions]


@router.post("/links", response_model=LinkResponse)
def create_link(
    link_data: LinkCreate = Body(...),
    db: Session = Depends(get_db),
    token: str = Depends(decode_access_token)
):
    if not token:
        raise HTTPException(status_code=401, detail="Token de acceso no proporcionado o no válido")
    
    try:
        belvo_client = get_belvo_client()
        response_data = belvo_client.Links.create(
            institution=link_data.institution,
            username=link_data.username,
            password=link_data.password
        )
        
        # Crear instancia del modelo SQLAlchemy con todos los campos necesarios
        new_link = Link(
            belvo_id=response_data['id'],
            institution=link_data.institution,
            username=link_data.username,
            access_mode=response_data.get("access_mode"),
            status=response_data.get("status"),
            refresh_rate=response_data.get("refresh_rate"),
            external_id=response_data.get("external_id"),
            institution_user_id=response_data.get("institution_user_id"),
            credentials_storage=response_data.get("credentials_storage"),
            stale_in=response_data.get("stale_in")
        )
        
        db.add(new_link)
        db.commit()
        db.refresh(new_link)

        return LinkResponse.from_orm(new_link)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating link: {str(e)}")