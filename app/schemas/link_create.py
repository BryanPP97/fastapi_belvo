from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional, List


class LinkCreate(BaseModel):
    institution: str
    username: str
    password: str


class LinkResponse(BaseModel):
    belvo_id: str
    institution: str
    access_mode: Optional[str] = "recurrent"
    status: Optional[str] = "valid"
    refresh_rate: Optional[str] = "7d"
    external_id: Optional[str]
    institution_user_id: Optional[str]
    credentials_storage: Optional[str]
    stale_in: Optional[str]
    fetch_resources: Optional[List[str]] = []

    class Config:
        from_attributes = True