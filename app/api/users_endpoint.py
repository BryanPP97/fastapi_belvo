from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.models.user import User
from app.models.link_create_models import Link
from app.schemas.user_schema import UserResponse
from app.schemas.link_create import LinkResponse
from app.core.auth import decode_access_token
from app.api.dependencies import validate_token

router = APIRouter()



@router.get("/user-links", response_model=list[LinkResponse])
def list_user_links(db: Session = Depends(get_db), token: str = Depends(validate_token)):
    user_links = db.query(Link).all()  # Aquí se cambió User por UserLink
    return user_links