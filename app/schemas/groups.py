from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class GroupBase(BaseModel):
    group_name: str

class GroupCreate(GroupBase):
    pass

class GroupResponse(GroupBase):
    id: int
    created_at: datetime
    created_by_id: int

    class Config:
        from_attributes = True
