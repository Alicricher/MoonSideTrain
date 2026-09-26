from fastapi import APIRouter
from storage import load_tasks, save_tasks

router = APIRouter()
@router.get("/tasks/search") 
def search_tasks(q: str):
    tasks = load_tasks()

    for task in tasks:
        if q.lower() in task["title"].lower():
            return task

    return {"message": "Task topilmadi"}
