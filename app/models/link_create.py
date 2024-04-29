from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.config import Base

class Link(Base):
    __tablename__ = 'links'
    
    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String(255))
    external_id = Column(String(255), nullable=True)
    access_mode = Column(String(50), nullable=False, default="recurrent")
    stale_in = Column(String(50), nullable=True)
    username_type = Column(String(50), nullable=True)
    last_accessed_at = Column(String(50), nullable=True)
    created_at = Column(String(50), nullable=True)
    status = Column(String(50), nullable=True)
    created_by = Column(String(255), nullable=True)
    refresh_rate = Column(String(50), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))   
    user = relationship("User", back_populates="links")