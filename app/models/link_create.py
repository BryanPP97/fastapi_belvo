from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.config import Base
from sqlalchemy.dialects.mysql import BINARY

class Link(Base):
    __tablename__ = 'links'
    
    id = Column(Integer, primary_key=True)  # ID interno como primary key
    belvo_id = Column(String(36), unique=True, nullable=False)
    institution = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    # Considera eliminar la columna de contraseña o asegúrate de que se almacene de forma segura
    # Agregar más campos conforme los necesitas de la respuesta de Belvo
    access_mode = Column(String(50))
    status = Column(String(50))
    refresh_rate = Column(String(50))
    external_id = Column(String(255))
    institution_user_id = Column(String(255))
    credentials_storage = Column(String(50))
    stale_in = Column(String(50))