from sqlalchemy import Column, String, DateTime
from app.core.config import Base
import os



class ListAllLinks(Base):
    __tablename__ = 'db_list_all_links'
    id = Column(String, primary_key=True)
    institution = Column(String)
    access_mode = Column(String)
    last_accessed_at = Column(DateTime)
    created_at = Column(DateTime)
    external_id = Column(String)
    institution_user_id = Column(String)
    status = Column(String)
    created_by = Column(String)
    refresh_rate = Column(String)
    credentials_storage = Column(String)
    stale_in = Column(String)






