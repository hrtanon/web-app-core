import json, os, pytest
from modules.taskmanager import TaskManager


# ── Fixture ────────────────────────────────────────────────

@pytest.fixture
def manager_with_tasks():
    """TaskManager s několika připravenými úkoly."""
    tm = TaskManager()
    tm.add_task("První úkol", "Popis prvního")
    tm.add_task("Druhý úkol", "Popis druhého")
    tm.add_task("Třetí úkol", "Popis třetího")
    return tm


# ── Přidání ────────────────────────────────────────────────

def test_add_task_increases_count():
    tm = TaskManager()
    tm.add_task("Nový")
    assert len(tm.get_all_tasks()) == 1


def test_add_multiple_tasks_get_unique_ids():
    tm = TaskManager()
    t1 = tm.add_task("Úkol 1")
    t2 = tm.add_task("Úkol 2")
    assert t1.task_id != t2.task_id


# ── Filtrování ─────────────────────────────────────────────

def test_filter_by_status_todo(manager_with_tasks):
    todos = manager_with_tasks.get_tasks_by_status("todo")
    assert len(todos) == 3


def test_filter_by_status_done(manager_with_tasks):
    manager_with_tasks.change_task_status(1, "done")
    done = manager_with_tasks.get_tasks_by_status("done")
    assert len(done) == 1
    assert done[0].task_id == 1


def test_filter_invalid_status_raises(manager_with_tasks):
    with pytest.raises(ValueError):
        manager_with_tasks.get_tasks_by_status("neplatny")


# ── Úpravy ─────────────────────────────────────────────────

def test_update_task_title(manager_with_tasks):
    manager_with_tasks.update_task(1, title="Nový název")
    task = manager_with_tasks.get_all_tasks()[0]
    assert task.title == "Nový název"


def test_update_nonexistent_raises(manager_with_tasks):
    with pytest.raises(KeyError):
        manager_with_tasks.update_task(999, title="X")


# ── Stav ───────────────────────────────────────────────────

def test_change_task_status(manager_with_tasks):
    manager_with_tasks.change_task_status(1, "in_progress")
    assert manager_with_tasks.get_all_tasks()[0].status == "in_progress"


def test_change_status_nonexistent_raises(manager_with_tasks):
    with pytest.raises(KeyError):
        manager_with_tasks.change_task_status(999, "done")


def test_change_status_invalid_value_raises(manager_with_tasks):
    with pytest.raises(ValueError):
        manager_with_tasks.change_task_status(1, "hotovo")


# ── Mazání ─────────────────────────────────────────────────

def test_delete_task_removes_it(manager_with_tasks):
    manager_with_tasks.delete_task(2)
    ids = [t.task_id for t in manager_with_tasks.get_all_tasks()]
    assert 2 not in ids


def test_delete_nonexistent_raises(manager_with_tasks):
    with pytest.raises(KeyError):
        manager_with_tasks.delete_task(999)


# ── JSON ───────────────────────────────────────────────────

def test_save_and_load_json(tmp_path):
    path = str(tmp_path / "tasks.json")
    tm = TaskManager()
    tm.add_task("Persistentní", "Popis")
    tm.change_task_status(1, "done")
    tm.save_to_json(path)

    tm2 = TaskManager()
    tm2.load_from_json(path)
    tasks = tm2.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title  == "Persistentní"
    assert tasks[0].status == "done"


def test_load_nonexistent_file_does_nothing(tmp_path):
    tm = TaskManager()
    tm.load_from_json(str(tmp_path / "neni.json"))
    assert tm.get_all_tasks() == []


def test_next_id_after_load(tmp_path):
    path = str(tmp_path / "tasks.json")
    tm = TaskManager()
    tm.add_task("A"); tm.add_task("B")
    tm.save_to_json(path)

    tm2 = TaskManager()
    tm2.load_from_json(path)
    new = tm2.add_task("C")
    assert new.task_id == 3