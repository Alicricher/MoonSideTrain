import json
from pathlib import Path


TASKS_FILE = Path(__file__).resolve().parent / "tasks.json"


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    with TASKS_FILE.open(encoding="utf-8") as file:
        return json.load(file)

def load_task(id):
    if not TASKS_FILE.exists():
        return []
    with TASKS_FILE.open(encoding="utf-8") as file:
        for task in tasks:
            if task["id"] == id:
                return task

def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)
        file.write("\n")
