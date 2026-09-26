# Task Manager API

Учебный проект на Python 3.10+ и FastAPI.
Задачи сохраняются в `tasks.json`, существующие данные совместимы.

## Запуск

Из папки репозитория:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

На Windows используйте `python` вместо `python3`, а для активации
в PowerShell — `.venv\Scripts\Activate.ps1`.
После установки зависимостей также можно запустить `python main.py`.

Откройте http://127.0.0.1:8000/docs — там можно вызывать API через
**Try it out → Execute**. Отдельного веб-интерфейса нет.

## API

| Метод | Адрес | Действие |
| --- | --- | --- |
| GET | `/tasks` | Список задач |
| POST | `/tasks` | Создание задачи, ответ 201 |
| PATCH | `/tasks/{task_id}/complete` | Завершение задачи |

Тело запроса для создания:

```json
{"title": "Learn Python"}
```

Ответ:

```json
{"id": 1, "title": "Learn Python", "status": "TODO"}
```

Завершение меняет статус на `DONE`. Несуществующая задача возвращает 404.
Пустое название, название только из пробелов и неверный тип данных
возвращают 422. Максимальная длина названия — 200 символов.

## Файлы

- `main.py` — FastAPI, маршруты и модели запросов/ответов.
- `task_manager.py` — операции с задачами.
- `storage.py` — чтение и запись JSON.
- `tasks.json` — данные.
- `test_api.py` — проверки API с отдельным временным файлом данных.

Хранилище JSON рассчитано на учебный запуск в одном процессе:
не запускайте несколько серверов или несколько workers с одним файлом.

## Проверка

```bash
python -m pip install -r requirements-dev.txt
python -m unittest -v
```

## Командная работа

Три задания на английском: [TASKS.md](TASKS.md).
Удаление, приоритеты и поиск оставлены для друзей.
Публикация, ветки и обязательные PR: [CONTRIBUTING.md](CONTRIBUTING.md).

Официальное руководство: https://fastapi.tiangolo.com/tutorial/first-steps/
