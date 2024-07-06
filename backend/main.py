from fastapi import FastAPI

from routes.group import group
from routes.task import task

app = FastAPI()
app.include_router(group)
app.include_router(task)
    