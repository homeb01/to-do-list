from models.task import Task

def task_entity(task: Task) -> dict:
    return {
        "id": str(task["_id"]),
        "description": task["description"],
        "completed": task["completed"],
        "dateTimeOfCreation": task["dateTimeOfCreation"],
    }
    
def tasks_entity(tasks: list) -> list:
    return [task_entity(task) for task in tasks]