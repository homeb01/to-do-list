from bson import ObjectId
from fastapi.routing import APIRouter

from routes.group import update_group
from models.task import Task
from schemas.task import tasks_entity
from models.group import Group
from config.db import db

task = APIRouter()

group_collection = db.get_collection("group")

@task.get("/group/{group_id}/tasks")
async def get_all_tasks(group_id: str):
    group = await group_collection.find_one({"_id": ObjectId(group_id)})
    tasks = group["tasks"]
    return tasks_entity(tasks)

@task.get("/{group_id}/{task_id}")
async def get_task(group_id: str, task_id: str):
    task = await group_collection.find_one({"_id": ObjectId(group_id), "tasks._id": ObjectId(task_id)})
    return tasks_entity(task)

@task.post("/{group_id}/tasks")
async def create_task(group_id: str, task: Task):
    update_group()
    new_group = dict(group)
    del new_group["id"]
    inserted_id = (await group_collection.insert_one(new_group)).inserted_id
    inserted_group = await group_collection.find_one({"_id": inserted_id})
    return group_entity(inserted_group)

@task.put("/group/{id}")
async def update_task(id: str, group: Group):
    await group_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(group)})
    return group_entity(await group_collection.find_one({"_id": ObjectId(id)}))

@task.delete("/group/{id}")
async def delete_task(id: str):
    return group_entity(await group_collection.find_one_and_delete({"_id": ObjectId(id)}))