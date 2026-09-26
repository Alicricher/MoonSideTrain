from fastapi import APIRouter
from storage import load_tasks, save_tasks

router = APIRouter()
@router.get("/tasks", response_model=list[Task])
def search_tasks():
        print("search_tasks called")
        print(load_tasks())
        return True
