from modules.taskmanager import TaskManager
from modules.task import ALLOWED_STATUSES

JSON_PATH = "data/tasks.json"

MENU = """
╔══════════════════════════════╗
║       TASK MANAGER           ║
╠══════════════════════════════╣
║  1. Přidat úkol              ║
║  2. Zobrazit všechny úkoly   ║
║  3. Filtrovat podle stavu    ║
║  4. Upravit úkol             ║
║  5. Změnit stav úkolu        ║
║  6. Smazat úkol              ║
║  7. Uložit úkoly             ║
║  8. Načíst úkoly             ║
║  0. Konec                    ║
╚══════════════════════════════╝
"""


def print_task_list(tasks):
    if not tasks:
        print("  (žádné úkoly)")
        return
    for task in tasks:
        print("-" * 40)
        print(task)
    print("-" * 40)


def get_int_input(prompt: str) -> int | None:
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("  Zadejte prosím číslo.")
        return None


def cmd_add_task(tm: TaskManager):
    title = input("Název úkolu: ").strip()
    description = input("Popis (nepovinný): ").strip()
    try:
        task = tm.add_task(title, description)
        print(f"  ✓ Úkol #{task.task_id} přidán.")
    except ValueError as e:
        print(f"  Chyba: {e}")


def cmd_show_all(tm: TaskManager):
    tasks = tm.get_all_tasks()
    print(f"\nCelkem úkolů: {len(tasks)}")
    print_task_list(tasks)


def cmd_filter_by_status(tm: TaskManager):
    print(f"  Dostupné stavy: {', '.join(sorted(ALLOWED_STATUSES))}")
    status = input("Stav: ").strip()
    try:
        tasks = tm.get_tasks_by_status(status)
        print(f"\nÚkoly se stavem '{status}': {len(tasks)}")
        print_task_list(tasks)
    except ValueError as e:
        print(f"  Chyba: {e}")


def cmd_update_task(tm: TaskManager):
    task_id = get_int_input("ID úkolu k úpravě: ")
    if task_id is None: return
    new_title = input("Nový název (Enter = beze změny): ").strip()
    new_desc  = input("Nový popis (Enter = beze změny): ").strip()
    try:
        tm.update_task(
            task_id,
            title       = new_title if new_title else None,
            description = new_desc  if new_desc  else None,
        )
        print("  ✓ Úkol upraven.")
    except (KeyError, ValueError) as e:
        print(f"  Chyba: {e}")


def cmd_change_status(tm: TaskManager):
    task_id = get_int_input("ID úkolu: ")
    if task_id is None: return
    print(f"  Dostupné stavy: {', '.join(sorted(ALLOWED_STATUSES))}")
    new_status = input("Nový stav: ").strip()
    try:
        task = tm.change_task_status(task_id, new_status)
        print(f"  ✓ Stav #{task.task_id} → '{task.status}'.")
    except (KeyError, ValueError) as e:
        print(f"  Chyba: {e}")


def cmd_delete_task(tm: TaskManager):
    task_id = get_int_input("ID úkolu ke smazání: ")
    if task_id is None: return
    confirm = input(f"  Opravdu smazat #{task_id}? (a/n): ").strip().lower()
    if confirm != "a":
        print("  Zrušeno."); return
    try:
        tm.delete_task(task_id)
        print(f"  ✓ Úkol #{task_id} smazán.")
    except KeyError as e:
        print(f"  Chyba: {e}")


def cmd_save(tm: TaskManager):
    try:
        tm.save_to_json(JSON_PATH)
        print(f"  ✓ Uloženo do {JSON_PATH}.")
    except Exception as e:
        print(f"  Chyba: {e}")


def cmd_load(tm: TaskManager):
    try:
        tm.load_from_json(JSON_PATH)
        print(f"  ✓ Načteno z {JSON_PATH}.")
    except Exception as e:
        print(f"  Chyba: {e}")


COMMANDS = {
    "1": cmd_add_task,
    "2": cmd_show_all,
    "3": cmd_filter_by_status,
    "4": cmd_update_task,
    "5": cmd_change_status,
    "6": cmd_delete_task,
    "7": cmd_save,
    "8": cmd_load,
}


def main():
    tm = TaskManager()
    try:
        tm.load_from_json(JSON_PATH)
        tasks = tm.get_all_tasks()
        if tasks:
            print(f"  Načteno {len(tasks)} úkolů z {JSON_PATH}.")
    except Exception:
        pass

    while True:
        print(MENU)
        choice = input("Volba: ").strip()
        if choice == "0":
            if input("Uložit před ukončením? (a/n): ").lower() == "a":
                cmd_save(tm)
            print("  Na shledanou!"); break
        handler = COMMANDS.get(choice)
        if handler:
            handler(tm)
        else:
            print("  Neplatná volba.")


if __name__ == "__main__":
    main()