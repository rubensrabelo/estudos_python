from datetime import datetime, timedelta
import pytest

from models.task import TaskModel
from db import db


@pytest.mark.parametrize(
        "task_name, expected_value",
        [
            ("Task 1", False),
            ("Another task", False),
            ("", False)
        ]
)
def test_task_model(client, task_name, expected_value):
    new_task = TaskModel(name=task_name)

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(name=task_name).first()

    assert task is not None
    assert task.name == task_name
    assert task.status == expected_value

    now = datetime.now()
    assert task.created_at <= now
    assert task.created_at >= now - timedelta(seconds=1)
    assert task.updated_at <= now
    assert task.updated_at >= now - timedelta(seconds=1)


@pytest.mark.parametrize(
        "initial_name, updated_name",
        [
            ("Initial Task", "Updated Task"),
            ("Another Task", "Another Updated Task"),
            ("Task Before", "Task After")
        ]
)
def test_task_update(client, initial_name, updated_name):
    new_task = TaskModel(name=initial_name)

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(name=initial_name).first()

    task.name = updated_name
    db.session.commit()

    update_task = TaskModel.query.filter_by(name=updated_name).first()

    assert update_task is not None
    assert update_task.name == updated_name
    assert update_task.updated_at >= task.created_at


@pytest.mark.parametrize(
        "task_name",
        ["Task to delete 1", "Task to delete 2", "Task to delete 3"]
)
def test_task_deletion(client, task_name):
    new_task = TaskModel(name=task_name)

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(name=task_name).first()

    db.session.delete(task)
    db.session.commit()

    deleted_task = TaskModel.query.filter_by(name=task_name).first()

    assert deleted_task is None


@pytest.mark.parametrize(
        "task_name, expected_status",
        [
            ("Task with status", True),
            ("Another Task", False)
        ]
)
def test_status_update(client, task_name, expected_status):
    new_task = TaskModel(name=task_name)

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(name=task_name).first()
    task.status = expected_status
    db.session.commit()

    update_task = TaskModel.query.filter_by(name=task_name).first()

    assert update_task is not None
    assert update_task.status is expected_status


def test_task_name_required(client):
    with pytest.raises(Exception) as e:
        new_task = TaskModel(name=None)
        db.session.add(new_task)
        db.session.commit()

    db.session.rollback()

    assert "IntegrityError" in str(e.type.__name__)


def test_query_by_id(client):
    new_task = TaskModel(name="Task by ID")

    db.session.add(new_task)
    db.session.commit()

    task = db.session.get(TaskModel, new_task.id)

    assert task is not None
    assert task.id == new_task.id
    assert task.name == "Task by ID"


def test_task_list(client):
    task1 = TaskModel(name="Task 1")
    task2 = TaskModel(name="Task 2")

    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()

    tasks = TaskModel.query.all()

    assert len(tasks) == 2


def test_transaction_rollback_on_error(client):
    try:
        task1 = TaskModel(name="Task before error")

        db.session.add(task1)

        task2 = TaskModel(name=None)

        db.session.add(task2)
        db.session.commit()
    except Exception:
        db.session.rollback()

    task = TaskModel.query.filter_by(name="Task Before Error").first()

    assert task is None
