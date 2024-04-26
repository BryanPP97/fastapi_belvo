from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.config import get_db
from ..core.security import get_current_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return security.verify_token(token, credentials_exception, db)
