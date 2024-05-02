from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.core.auth import decode_access_token
from app.models.link_create_models import Link
from app.schemas.link_create import LinkCreate, LinkResponse
from app.api.dependencies import get_db
from app.core.config import get_belvo_client
from typing import List


router = APIRouter()


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