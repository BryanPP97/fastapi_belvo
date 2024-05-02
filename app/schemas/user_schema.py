from pydantic import BaseModel

class UserResponse(BaseModel):
    link_id: str
    institution: str
    access_mode: str
    status: str
    refresh_rate: str
    external_id: str
    institution_user_id: str
    credentials_storage: str
    stale_in: str

    class Config:
        orm_mode = True

from pydantic import BaseModel

class UserLinkResponse(BaseModel):
    link_id: str
    institution: str
    access_mode: str
    status: str
    refresh_rate: str
    external_id: str
    institution_user_id: str
    credentials_storage: str
    stale_in: str

    class Config:
        orm_mode = True
