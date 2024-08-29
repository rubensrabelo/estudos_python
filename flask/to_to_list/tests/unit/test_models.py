from datetime import datetime, timedelta

from models.task import TaskModel
from db import db


# 1. Task creation test
def test_task_model(client):
    new_task = TaskModel(name="Test Task")

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(name="Test Task").first()

    assert task is not None
    assert task.name == "Test Task"
    assert task.status is False

    now = datetime.now()
    assert task.created_at <= now
    assert task.created_at >= now - timedelta(seconds=1)
    assert task.updated_at <= now
    assert task.updated_at >= now - timedelta(seconds=1)


# 2. Task update task
def test_task_update(client):
    new_task = TaskModel(name="Test Task")

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(name="Test Task").first()

    task.name = "Update Task"
    db.session.commit()

    update_task = TaskModel.query.filter_by(name="Update Task").first()

    assert update_task is not None
    assert update_task.name == "Update Task"
    assert update_task.updated_at > task.created_at
