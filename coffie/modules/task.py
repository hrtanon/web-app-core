# Povolené hodnoty stavu úkolu – sdílené s TaskManagerem
ALLOWED_STATUSES = {"todo", "in_progress", "done"}


class Task:
    """Reprezentuje jeden konkrétní úkol."""

    def __init__(self, task_id: int, title: str,
                 description: str = "", status: str = "todo"):
        if not title or not title.strip():
            raise ValueError("Název úkolu nesmí být prázdný.")
        if status not in ALLOWED_STATUSES:
            raise ValueError(
                f"Neplatný stav '{status}'. Povolené stavy: {ALLOWED_STATUSES}"
            )
        self.task_id     = task_id
        self.title       = title.strip()
        self.description = description
        self.status      = status

    def change_status(self, new_status: str) -> None:
        """Změní stav úkolu na novou hodnotu."""
        if new_status not in ALLOWED_STATUSES:
            raise ValueError(
                f"Neplatný stav '{new_status}'. Povolené stavy: {ALLOWED_STATUSES}"
            )
        self.status = new_status

    def update_title(self, new_title: str) -> None:
        """Upraví název úkolu."""
        if not new_title or not new_title.strip():
            raise ValueError("Název úkolu nesmí být prázdný.")
        self.title = new_title.strip()

    def update_description(self, new_description: str) -> None:
        """Upraví popis úkolu."""
        self.description = new_description

    def to_dict(self) -> dict:
        """Převede objekt Task na slovník pro serializaci."""
        return {
            "task_id":     self.task_id,
            "title":       self.title,
            "description": self.description,
            "status":      self.status,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Vytvoří objekt Task ze slovníku."""
        return cls(
            task_id     = data["task_id"],
            title       = data["title"],
            description = data.get("description", ""),
            status      = data.get("status", "todo"),
        )

    def __str__(self) -> str:
        status_label = {
            "todo":        "[ ] Todo",
            "in_progress": "[~] In Progress",
            "done":        "[✓] Done",
        }.get(self.status, self.status)
        lines = [
            f"ID: {self.task_id}  {status_label}",
            f"Název: {self.title}",
        ]
        if self.description:
            lines.append(f"Popis: {self.description}")
        return "\n".join(lines)