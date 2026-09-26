def add_task(tasks, title):
    task_id = max((task["id"] for task in tasks), default=0) + 1
    task = {"id": task_id, "title": title, "status": "TODO"}
    tasks.append(task)
    return task


def list_tasks(tasks):
    if not tasks:
        print("Пока задач нет.")
        return

    for task in tasks:
        print(f"ID: {task['id']} | {task['title']} | {task['status']}")


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "DONE"
            return True
    return False
