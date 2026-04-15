from pydantic import BaseModel
from datetime import datetime

class SidebarItem(BaseModel):
    id: int
    type: str
    name: str
    last_activity_time: datetime
    latest_message_snippet: str

    class Config:
        from_attributes = True
