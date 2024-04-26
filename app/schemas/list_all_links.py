from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ListAllLinksSchema(BaseModel):
    id: str
    institution: str
    access_mode: str
    last_accessed_at: datetime
    created_at: datetime
    external_id: str
    institution_user_id: str
    status: str
    created_by: str
    refresh_rate: str
    credentials_storage: str
    fetch_resources: List[str]
    stale_in: str

class Config:
        orm_mode = True