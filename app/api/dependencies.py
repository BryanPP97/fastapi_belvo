from app.core.config import SessionLocal
from fastapi import APIRouter, HTTPException, Depends
from app.core.auth import decode_access_token   


def get_db():
    db = SessionLocal()
    try:
        yield db #Asegura que la sesión solo se mantenga abierta durante el tiempo necesario para procesar la solicitud.
    finally:
        db.close()

def validate_token(token: str = Depends(decode_access_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Token de acceso no proporcionado o no válido")

