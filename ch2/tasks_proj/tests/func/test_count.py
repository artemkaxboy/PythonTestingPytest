"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task


def test_count_zero_tasks_when_db_empty():
    """Calling tasks.count() on an empty db should return zero."""
    # GIVEN an initialized tasks db
    # WHEN nothing is added
    # THEN the count of tasks is zero
    assert tasks.count() == 0


def test_count_one_task_when_db_has_one_task():
    """Calling tasks.count() on a db with one item should return 1."""
    # GIVEN an initialized tasks db
    #   AND a new task is added
    new_task = Task('do something')
    tasks.add(new_task)

    # WHEN the number of tasks is counted
    # THEN the count is 1
    assert tasks.count() == 1


@pytest.mark.parametrize('expected_count', (0, 1, 2, 100))
def test_count_n_tasks_when_db_has_n_tasks(expected_count):
    """Calling tasks.count() on a db with two items should return 2."""
    # GIVEN an initialized tasks db
    #   AND n new tasks are added
    task = Task('first')
    for i in range(expected_count):
        tasks.add(task)

    # WHEN the number of tasks is counted
    # THEN the count is n
    assert tasks.count() == expected_count


def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    """Make sure the task_id field is set by tasks.add()."""
    # GIVEN an initialized tasks db
    #   AND a new task is added
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    # WHEN task is retrieved
    task_from_db = tasks.get(task_id)

    # THEN task_id matches id field
    assert task_from_db.id == task_id


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
