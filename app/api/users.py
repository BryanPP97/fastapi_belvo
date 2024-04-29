from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.models.user import User
from app.schemas.user_schema import UserResponse
from app.core.auth import decode_access_token

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])  
def list_users(
    db: Session = Depends(get_db),
    token: str = Depends(decode_access_token)
):
    if not token:
        raise HTTPException(status_code=401, detail="Token de acceso no proporcionado o no válido")
    try:
        users = db.query(User).all()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error processing transactions: {str(e)}")

    return users