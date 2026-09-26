# Team Assignments — FastAPI

Each person implements one feature in a separate branch and opens a Pull
Request into `main`. Ask a teammate to review it and get at least one
approval before merging. See [CONTRIBUTING.md](CONTRIBUTING.md).

Start the API using the README instructions. Use http://127.0.0.1:8000/docs
and **Try it out** to test requests.

## Task 1: Delete a Task

**Branch:** `feature/delete-task`

- Add `delete_task(tasks, task_id)` in `task_manager.py`; return a boolean.
- Add `DELETE /tasks/{task_id}` in `main.py` with an integer task ID.
- Load tasks, delete the matching task, and save the updated list.
- Use the existing `tasks_lock` around the entire read-modify-write operation.
- Return HTTP 204 with no response body on success.
- Return HTTP 404 if the task does not exist.
- Keep the IDs of the remaining tasks unchanged.

Check: delete one of two tasks; confirm it stays deleted after restarting.
Try an unknown ID (404), a non-integer ID (422), and an empty task list (404).

## Task 2: Task Priority

**Branch:** `feature/task-priority`

- Update `add_task(tasks, title, priority="MEDIUM")` to store a priority.
- Add a priority field to `TaskCreate` and `Task` in `main.py`.
- Allow only `LOW`, `MEDIUM`, and `HIGH`; default to `MEDIUM` when omitted.
- Accept lowercase input by converting it to uppercase before validation.
- Invalid values must return HTTP 422.
- Return the priority in creation, listing, and completion responses.
- Save priorities to JSON.
- Older tasks without a priority field must still work and return `MEDIUM`.

Example request to `POST /tasks`:

```json
{"title": "Learn Python", "priority": "HIGH"}
```

Check all priorities, lowercase input, omitted priority, and an invalid value.
Restart and confirm priorities persist. Test an older task without the field.

## Task 3: Search Tasks

**Branch:** `feature/search-tasks`

- Add `search_tasks(tasks, query)` in `task_manager.py`.
- Return matching tasks without modifying the original list.
- Match a substring of the title, ignoring case.
- Strip leading and trailing spaces from the query.
- Return an empty list for an empty or whitespace-only query.
- Add `GET /tasks/search?q=python` with a required string query parameter `q`.
- Return HTTP 200 and a JSON list of tasks; return `[]` if nothing matches.
- Use `response_model=list[Task]` and the existing lock when loading tasks.
- Search both TODO and DONE tasks. Do not write to `tasks.json`.

Check: create `Learn Python`, `Python homework`, and `Buy milk`.
Searching for `python`, `PYTHON`, or ` python ` should return the first two.
Try an unmatched word, an empty query, and an empty task list.
Omitting `q` entirely should return 422.

## Before Opening Your Pull Request

- Check your feature through `/docs`.
- Confirm that creating, listing, and completing tasks still work.
- Run `python -m unittest -v` after installing `requirements-dev.txt`.
- Include only feature changes; do not commit personal test tasks.
- Describe your changes and checks in the PR.
- If another feature merges first, merge the latest `origin/main` into your
  branch, resolve conflicts, and check the API again.
