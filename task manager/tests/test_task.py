from modules import Task





def test_task_creation():
    task = Task(1, "Nakoupit", "Mléko", "todo")

    assert task.task_id == 1
    assert task.title == "Nakoupit"
    assert task.description == "Mléko"
    assert task.status == "todo"
    
def test_valid_status_change():
    task = Task(1, "A", "B", "todo")

    task.change_status("done")

    assert task.status == "done"


def test_invalid_status_change():
    task = Task(1, "A", "B", "todo")

    old_status = task.status
    task.change_status("invalid")

    assert task.status == old_status
    

def test_update_title_and_description():
    task = Task(1, "A", "B", "todo")

    task.change_title("Nový název")
    task.change_description("Nový popis")

    assert task.title == "Nový název"
    assert task.description == "Nový popis"



def test_to_dict():
    task = Task(1, "A", "B", "todo")

    data = task.to_dict()

    assert data["task_id"] == 1
    assert data["title"] == "A"
    assert data["description"] == "B"
    assert data["status"] == "todo"


