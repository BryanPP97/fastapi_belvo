from sqlalchemy import Column, Integer, String
from app.core.config import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    password = Column(String(255))

class UserLink(Base):
    __tablename__ = 'users_link'
    
    id = Column(Integer, primary_key=True)
    link_id = Column(String(255), unique=True)
    institution = Column(String(255))
    access_mode = Column(String(255))
    status = Column(String(255))
    refresh_rate = Column(String(255))
    external_id = Column(String(255), nullable=True)
    institution_user_id = Column(String(255))
    credentials_storage = Column(String(255))
    stale_in = Column(String(255), nullable=True)