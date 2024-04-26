from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Message(BaseModel):
    id: UUID
    user_id: UUID
    channel_id: UUID
    content: str
    timestamp: datetime