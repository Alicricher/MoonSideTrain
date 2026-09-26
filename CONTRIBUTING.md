# Работа через ветки и Pull Request

## Владельцу: первая публикация

Репозиторий уже создан локально, базовая ветка — `main`.
В GitHub Desktop выберите этот репозиторий и нажмите Publish repository.
Либо создайте пустой репозиторий на GitHub (без README и .gitignore), затем:

```bash
git remote add origin https://github.com/YOUR_LOGIN/MoonSideTrain.git
git push -u origin main
```

Замените YOUR_LOGIN своим логином. Используйте один из способов публикации.

## Обязательные PR на GitHub

После первого push:

1. Settings → Collaborators → добавьте друзей с правом записи.
2. Settings → Branches → Add classic branch protection rule.
3. Branch name pattern: `main`.
4. Включите Require a pull request before merging.
5. Включите Require approvals, количество — 1.
6. Включите Dismiss stale pull request approvals when new commits are pushed.
7. Включите Require conversation resolution before merging.
8. Включите Do not allow bypassing the above settings, чтобы правило действовало и для администратора.
9. Оставьте Allow force pushes и Allow deletions выключенными, сохраните правило.

Это запрещает прямой push в main и требует одобрения другого участника.
Договоритесь отдельно, что кнопку Merge нажимает другой участник:
одобрение не запрещает автору нажать Merge после получения approve.

Защита веток доступна в публичных репозиториях на GitHub Free.
Для приватного репозитория нужен подходящий платный тариф (например, Pro
для личного аккаунта). Локальные настройки Git не заменяют защиту на сервере.

Документация: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches

## Каждому другу

Один раз клонируйте опубликованный репозиторий:

```bash
git clone https://github.com/YOUR_LOGIN/MoonSideTrain.git
cd MoonSideTrain
```

Перед началом фичи (рабочая папка должна быть без незакоммиченных изменений):

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/delete-task
```

Ветки друзей:

- `feature/delete-task` — удаление задачи.
- `feature/task-priority` — приоритет.
- `feature/search-tasks` — поиск.

Установите зависимости по README. После написания кода проверьте API
через http://127.0.0.1:8000/docs, остановите сервер (Ctrl+C) и сделайте коммит:

```bash
python -m uvicorn main:app --reload
git status
git diff
git add main.py task_manager.py
git commit -m "Add task deletion"
git push -u origin feature/delete-task
```

Укажите свои изменённые файлы в git add и используйте имя своей ветки.
Не коммитьте личные задачи из tasks.json.

На GitHub: Compare & pull request → base: main → Create pull request.
Друг открывает Files changed → Review changes → Approve либо Request changes.
Исправления коммитятся и отправляются через git push в ту же ветку;
PR обновляется автоматически. После одобрения другой участник нажимает Merge.

После merge:

```bash
git switch main
git pull --ff-only origin main
```

Следующую фичу начинайте в новой ветке от обновлённой main.

## Если возник конфликт

В своей feature-ветке с сохранёнными в коммите изменениями:

```bash
git fetch origin
git merge origin/main
```

Исправьте конфликтующие файлы: объедините нужный код и удалите маркеры
`<<<<<<<`, `=======`, `>>>>>>>`. Проверьте API через /docs, затем:

```bash
git add main.py task_manager.py
git commit -m "Resolve merge conflict with main"
git push
```

В git add укажите именно исправленные файлы. Если хотите отменить
незавершённое слияние, используйте `git merge --abort`.
