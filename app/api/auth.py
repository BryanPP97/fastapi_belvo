from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.auth import create_access_token
from app.models.user import User
from app.api.dependencies import get_db
from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.core.security import verify_password
from app.schemas.user_schema import UserResponse

router = APIRouter()

@router.post("/login")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    # Si las credenciales son válidas, genera un token de acceso
    token_data = {"username": form_data.username}
    access_token = create_access_token(data=token_data)
    
    # Devuelve el token de acceso
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
def register_user(username: str, password: str, db: Session = Depends(get_db)):
    # Verifica si el usuario ya existe en la base de datos
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    # Crea el nuevo usuario en la base de datos
    hashed_password = hash_password(password)
    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    db.commit()
    
    # Devuelve una confirmación de que el usuario ha sido creado
    return {"message": "Usuario creado exitosamente"}
