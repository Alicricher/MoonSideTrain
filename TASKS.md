# Team Assignments

Each person picks one task and implements it in a separate branch.
Start from the latest `main`, open a Pull Request into `main`, and ask a
teammate to review it. Get at least one approval before merging.
See [CONTRIBUTING.md](CONTRIBUTING.md) for Git commands.

## Task 1: Delete a Task

**Branch:** `feature/delete-task`

Add the ability to delete a task by its ID.

Requirements:

- Add `delete_task(tasks, task_id)` to `task_manager.py`.
- Return `True` if a task was deleted and `False` if the ID was not found.
- Add a "Delete task" option to the menu in `main.py`.
- Ask the user for a task ID and handle input that is not a number.
- Display a clear message when the task does not exist.
- Save the updated list using `save_tasks(tasks)` after deletion.
- Keep the IDs of the remaining tasks unchanged.

Manual checks:

1. Create two tasks and delete one of them.
2. Show the list and confirm that only the selected task was removed.
3. Restart the program and confirm that the deleted task stays deleted.
4. Try an unknown ID, non-numeric input, and deletion from an empty list.

## Task 2: Task Priority

**Branch:** `feature/task-priority`

Add a priority to each task: `LOW`, `MEDIUM`, or `HIGH`.

Requirements:

- Update the function to `add_task(tasks, title, priority="MEDIUM")`.
- Ask for a priority when creating a task.
- Accept lowercase input by converting it to uppercase.
- Use `MEDIUM` when the user leaves the input empty.
- For any other value, show an error and ask again.
- Store the priority in the task dictionary and save it to JSON.
- Display the priority when listing tasks.
- Older tasks without a priority field must still work: display `MEDIUM`
  for them. Hint: use `task.get("priority", "MEDIUM")`.

Manual checks:

1. Create tasks with each of the three priorities.
2. Check lowercase input, empty input, and an invalid value.
3. Restart the program and confirm that priorities are preserved.
4. Confirm that a task without a priority field can still be displayed.

## Task 3: Search Tasks

**Branch:** `feature/search-tasks`

Add the ability to find tasks by part of their title.

Requirements:

- Add `search_tasks(tasks, query)` to `task_manager.py`.
- Return a list of matching tasks without changing the original list.
- Make matching case-insensitive: `python` must match `Learn Python`.
- Remove spaces from the beginning and end of the query.
- Return an empty list for an empty query.
- Add a "Search tasks" option to the menu in `main.py`.
- Show matching tasks using the existing `list_tasks()` function.
- If there are no matches, display "No matching tasks found."
- Search both TODO and DONE tasks. Searching must not change `tasks.json`.

Manual checks:

1. Create `Learn Python`, `Python homework`, and `Buy milk`.
2. Search for `python`: the first two tasks should appear.
3. Try `PYTHON` and ` python `: the results should be the same.
4. Try an unmatched word, an empty query, and an empty task list.

## Before Opening Your Pull Request

- Run `python3 main.py` and complete the manual checks for your task.
- Confirm that adding, listing, completing, and exiting still work.
- Keep all menu numbers unique and update the invalid-choice message.
- Include only your feature changes; do not commit personal test tasks.
- Describe what you changed and how you checked it in the PR.
- If another feature is merged first, merge the latest `origin/main` into
  your branch, resolve any conflicts, and check the program again.
