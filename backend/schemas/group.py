from models.group import Group

def group_entity(group: Group) -> dict:
    return {
        "id": str(group["_id"]),
        "name": group["name"],
        "dateTimeOfCreation": group["dateTimeOfCreation"],
        "tasks": group["tasks"]
    }
    
def groups_entity(groups: list) -> list:
    return [group_entity(group) for group in groups]