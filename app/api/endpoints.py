from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.list_all_links import ListAllLinks
from app.schemas.list_all_links import ListAllLinksSchema
from app.core.config import SessionLocal
from app.core.config import get_belvo_client


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/list-all-links")
def create_institution(listalllinks: ListAllLinksSchema, db: Session = Depends(get_db)):
    db_list_all_links = ListAllLinks(**listalllinks.dict())
    db.add(db_list_all_links)
    db.commit()
    db.refresh(db_list_all_links)
    return db_list_all_links
