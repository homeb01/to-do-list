from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel

class Task(BaseModel):
    id: Optional[str] = None
    description: str
    completed: bool
    dateTimeOfCreation: datetime
    class Config:
        schema_extra = {
            "example": {
                "description": "Do homework",
                "completed": "false",
                "dateTimeOfCreation": "2024-06-17T01:40:15Z"
            }
        }