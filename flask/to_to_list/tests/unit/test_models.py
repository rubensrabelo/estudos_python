from models.task import TaskModel
from db import db


def test_task_model(client):
    new_task = TaskModel(title="Test Task", description="This is a test task")

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(title="Test Task").first()

    assert task is not None
    assert task.title == "Test Task"
    assert task.status == False
    assert task.description == "This is a test task"
