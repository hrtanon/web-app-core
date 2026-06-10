import pytest
from modules.task import Task


def test_task_creation_sets_attributes():
    task = Task(task_id=1, title="Napsat testy",
                description="Pro Task a TaskManager")
    assert task.task_id == 1
    assert task.title == "Napsat testy"
    assert task.description == "Pro Task a TaskManager"
    assert task.status == "todo"


def test_task_default_status_is_todo():
    task = Task(task_id=2, title="Nový úkol")
    assert task.status == "todo"


def test_task_strips_whitespace_from_title():
    task = Task(task_id=3, title="  Mezery kolem  ")
    assert task.title == "Mezery kolem"


def test_task_empty_title_raises():
    with pytest.raises(ValueError):
        Task(task_id=4, title="")


def test_task_whitespace_only_title_raises():
    with pytest.raises(ValueError):
        Task(task_id=5, title="   ")


def test_task_invalid_status_raises():
    with pytest.raises(ValueError):
        Task(task_id=6, title="Úkol", status="neplatny_stav")


def test_change_status_to_in_progress():
    task = Task(task_id=7, title="Úkol")
    task.change_status("in_progress")
    assert task.status == "in_progress"


def test_change_status_invalid_raises():
    task = Task(task_id=8, title="Úkol")
    with pytest.raises(ValueError):
        task.change_status("splneno")


def test_update_title():
    task = Task(task_id=9, title="Starý")
    task.update_title("Nový")
    assert task.title == "Nový"


def test_update_title_empty_raises():
    task = Task(task_id=10, title="Název")
    with pytest.raises(ValueError):
        task.update_title("")


def test_to_dict_returns_correct_structure():
    task = Task(task_id=11, title="Dict",
                description="Popis", status="in_progress")
    assert task.to_dict() == {
        "task_id": 11, "title": "Dict",
        "description": "Popis", "status": "in_progress"
    }


def test_roundtrip_to_dict_and_back():
    orig = Task(task_id=12, title="Roundtrip",
               description="Test", status="done")
    rest = Task.from_dict(orig.to_dict())
    assert rest.task_id == orig.task_id
    assert rest.title   == orig.title
    assert rest.status  == orig.status


def test_str_contains_title_and_status():
    task = Task(task_id=13, title="Zobrazení")
    text = str(task)
    assert "Zobrazení" in text
    assert "Todo" in text