from sqlalchemy import Column, String, DateTime, Integer
from app.core.config import Base

class Link(Base):
    __tablename__ = 'links'
    
    id = Column(Integer, primary_key=True)  # ID interno como primary key
    belvo_id = Column(String(36), unique=True, nullable=False, index=True)
    institution = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)  
    access_mode = Column(String(50))
    status = Column(String(50))
    refresh_rate = Column(String(50))
    external_id = Column(String(255))
    institution_user_id = Column(String(255))
    credentials_storage = Column(String(50))
    stale_in = Column(String(50))