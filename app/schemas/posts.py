from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    group_id: Optional[int] = None
    recipient_id: Optional[int] = None

class PostCreate(PostBase):
    pass # The actual file upload will be handled by FastAPI's UploadFile

class PostResponse(PostBase):
    id: int
    file_url: str
    file_type: str
    owner_id: int
    is_deleted: bool

    class Config:
        from_attributes = True