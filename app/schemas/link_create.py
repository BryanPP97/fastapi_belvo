from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class LinkCreate(BaseModel):
    institution: str
    username: str
    password: Optional[str] = None
    external_id: Optional[str] = None
    username2: Optional[str] = None
    username3: Optional[str] = None
    password2: Optional[str] = None
    token: Optional[str] = None
    access_mode: str = Field(default="recurrent")
    username_type: Optional[str] = None

class LinkResponse(BaseModel):
    id: str
    institution: str
    access_mode: str
    last_accessed_at: Optional[datetime]
    created_at: datetime
    external_id: Optional[str]
    institution_user_id: Optional[str]
    status: str
    created_by: Optional[str]
    username_type: Optional[str]

    class Config:
        orm_mode = True