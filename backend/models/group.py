from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from models.task import Task


class Group(BaseModel):
    id: Optional[str] = None
    name: str
    dateTimeOfCreation: datetime
    tasks: List[Task]
    class Config:
        schema_extra = {
            "example": {
                "name": "Personal",
                "dateTimeOfCreation": "2024-06-17T01:40:15Z",
                "tasks": [
                    {
                        "description": "Do homework",
                        "completed": "false",
                        "dateTimeOfCreation": "2024-06-17T01:40:15Z"
                    },
                ]
            }
        }