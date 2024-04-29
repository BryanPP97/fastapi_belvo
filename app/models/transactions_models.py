from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.config import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, index=True)
    link_id = Column(String(255), index=True)
    account_id = Column(String(255), index=True)
    amount = Column(Float)
    currency = Column(String(3))
    collected_at = Column(DateTime)
    status = Column(String(50))
    type = Column(String(50))
