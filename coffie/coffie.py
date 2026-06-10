import json
import os
from modules.task import Task, ALLOWED_STATUSES

DEFAULT_JSON_PATH = "data/tasks.json"


class TaskManager:
    """Spravuje kolekci úkolů."""

    def __init__(self):
        self._tasks: list[Task] = []
        self._next_id: int = 1

    # ── Přidání a získání ──────────────────────────────────────

    def add_task(self, title: str, description: str = "") -> Task:
        """Přidá nový úkol a vrátí jej."""
        task = Task(task_id=self._next_id, title=title,
                    description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Vrátí kopii seznamu všech úkolů."""
        return list(self._tasks)

    def get_tasks_by_status(self, status: str) -> list[Task]:
        """Vrátí seznam úkolů s daným stavem."""
        if status not in ALLOWED_STATUSES:
            raise ValueError(
                f"Neplatný stav '{status}'."
            )
        return [t for t in self._tasks if t.status == status]

    def _find_task(self, task_id: int) -> Task:
        """Interní: najde úkol podle ID nebo vyhodí KeyError."""
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        raise KeyError(f"Úkol s ID {task_id} neexistuje.")

    # ── Úpravy a mazání ───────────────────────────────────────

    def update_task(self, task_id: int,
                   title: str | None = None,
                   description: str | None = None) -> Task:
        """Upraví název a/nebo popis úkolu podle ID."""
        task = self._find_task(task_id)
        if title is not None:
            task.update_title(title)
        if description is not None:
            task.update_description(description)
        return task

    def change_task_status(self, task_id: int,
                          new_status: str) -> Task:
        """Změní stav úkolu podle ID."""
        task = self._find_task(task_id)
        task.change_status(new_status)
        return task

    def delete_task(self, task_id: int) -> None:
        """Smaže úkol podle ID."""
        task = self._find_task(task_id)
        self._tasks.remove(task)

    # ── JSON persistence ──────────────────────────────────────

    def save_to_json(self, path: str = DEFAULT_JSON_PATH) -> None:
        """Uloží všechny úkoly do JSON souboru."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                [t.to_dict() for t in self._tasks],
                f, ensure_ascii=False, indent=4
            )

    def load_from_json(self, path: str = DEFAULT_JSON_PATH) -> None:
        """Načte úkoly z JSON souboru. Přepíše aktuální seznam."""
        if not os.path.exists(path):
            return
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self._tasks = [Task.from_dict(item) for item in data]
        if self._tasks:
            self._next_id = max(t.task_id for t in self._tasks) + 1
        else:
            self._next_id = 1