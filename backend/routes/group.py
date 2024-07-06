from bson import ObjectId
from fastapi.routing import APIRouter

from schemas.group import group_entity, groups_entity
from models.group import Group
from config.db import db

group = APIRouter()

group_collection = db.get_collection("group")

@group.get("/group")
async def get_all_groups():
    groups = await group_collection.find().to_list(None)
    return groups_entity(groups)

@group.get("/group/{id}")
async def get_group(id: str):
    group = await group_collection.find_one({"_id": ObjectId(id)})
    return group_entity(group)

@group.post("/group")
async def create_group(group: Group):
    new_group = dict(group)
    del new_group["id"]
    inserted_id = (await group_collection.insert_one(new_group)).inserted_id
    inserted_group = await group_collection.find_one({"_id": inserted_id})
    return group_entity(inserted_group)

@group.put("/group/{id}")
async def update_group(id: str, group: Group):
    await group_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(group)})
    return group_entity(await group_collection.find_one({"_id": ObjectId(id)}))

@group.delete("/group/{id}")
async def delete_group(id: str):
    return group_entity(await group_collection.find_one_and_delete({"_id": ObjectId(id)}))