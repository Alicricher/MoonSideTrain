from threading import Lock
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

from storage import load_tasks, save_tasks
from task_manager import add_task, complete_task, list_tasks


app = FastAPI(title="Task Manager API")
# Protect JSON read-modify-write operations within a single server process.
tasks_lock = Lock()


class TaskCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str = Field(min_length=1, max_length=200)


class Task(BaseModel):
    id: int
    title: str
    status: Literal["TODO", "DONE"]


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    with tasks_lock:
        return list_tasks(load_tasks())


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(body: TaskCreate):
    with tasks_lock:
        tasks = load_tasks()
        task = add_task(tasks, body.title)
        save_tasks(tasks)
        return task


@app.patch("/tasks/{task_id}/complete", response_model=Task)
def finish_task(task_id: int):
    with tasks_lock:
        tasks = load_tasks()
        task = complete_task(tasks, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        save_tasks(tasks)
        return task


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
