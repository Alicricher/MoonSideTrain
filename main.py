from storage import load_tasks, save_tasks
from task_manager import add_task, complete_task, list_tasks


def main():
    try:
        tasks = load_tasks()
    except (OSError, ValueError) as error:
        print(f"Не удалось загрузить задачи: {error}")
        return

    while True:
        print("\n=== Task Manager ===")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Завершить задачу")
        print("4. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Название задачи: ").strip()
            if not title:
                print("Название не может быть пустым.")
                continue
            add_task(tasks, title)
        elif choice == "2":
            list_tasks(tasks)
            continue
        elif choice == "3":
            try:
                task_id = int(input("ID задачи: "))
            except ValueError:
                print("Введите целое число.")
                continue
            if not complete_task(tasks, task_id):
                print("Задача не найдена.")
                continue
        elif choice == "4":
            print("До встречи!")
            break
        else:
            print("Выберите пункт от 1 до 4.")
            continue

        try:
            save_tasks(tasks)
            print("Изменения сохранены.")
        except OSError as error:
            print(f"Не удалось сохранить задачи: {error}")


if __name__ == "__main__":
    main()
