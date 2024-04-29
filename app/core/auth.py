import jwt
from datetime import datetime, timedelta
from typing import Optional
from app.core.config import SECRET_KEY

# Define el tiempo de expiración del token (en minutos)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict) -> str:
    """
    Genera un token de acceso JWT con la información proporcionada en los datos.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def decode_access_token(token: str) -> Optional[dict]:
    """
    Decodifica y verifica un token de acceso JWT.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        # Token ha expirado
        return None
    except jwt.InvalidTokenError:
        # Token no válido
        return None
