
from modules.taskmanager import Taskmanage



    



def test_add_task():
    manager = Taskmanage()

    manager.novy_task("A", "B", "todo")

    assert len(manager.tasks) == 1





def test_get_all():
    manager = Taskmanage()
    manager.novy_task("A", "B", "todo")

    tasks = manager.seznam()

    assert len(tasks) == 1




def test_change_status():
    manager = Taskmanage()

    manager.novy_task("A", "B", "todo")

    task = manager.zmena_status_dleid(1, "done")

    assert task.status == "done"


def test_update_task():
    manager = Taskmanage()

    manager.novy_task("A", "B", "todo")

    manager.uprav(1, title="X", description="Y")

    task = manager.najit(1)

    assert task.title == "X"
    assert task.description == "Y"





def test_delete_task():
    manager = Taskmanage()

    manager.novy_task("A", "B", "todo")

    manager.smaz(1)

    assert len(manager.tasks) == 0




def test_invalid_id():
    manager = Taskmanage()

    result = manager.najit(999)

    assert result is None


def test_empty_title():
    manager = Taskmanage()

    result = manager.novy_task("", "desc", "todo")

    assert result.title != ""