from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.sql import func
from app.core.config import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    transaction_id = Column(String(255), index=True)
    link_id = Column(String(255), index=True)
    account_id = Column(String(255), index=True)
    account_name = Column(String(255), index=True)
    account_type = Column(String(255), index=True)
    transaction_category = Column(String(255))
    transaction_type = Column(String(50))
    amount = Column(Float)
    status = Column(String(50))
    currency = Column(String(10))
    description = Column(String(255))
    username = Column(String(255), ForeignKey('users.username'))

    
    
    
    
    
