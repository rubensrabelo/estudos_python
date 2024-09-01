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
    assert task.id == 1
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


# 3. Teste de exclusão de tarefa
def test_task_deletion(client):
    new_task = TaskModel(name="Task to delete")

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(name="Task to delete").first()

    db.session.delete(task)
    db.session.commit()

    deleted_task = TaskModel.query.filter_by(name="Task to delete").first()

    assert deleted_task is None


# 4. Teste de status da tarefa
def test_status_update(client):
    new_task = TaskModel(name="Task with status")

    db.session.add(new_task)
    db.session.commit()

    task = TaskModel.query.filter_by(name="Task with status").first()
    task.status = True
    db.session.commit()

    update_task = TaskModel.query.filter_by(name="Task with status").first()

    assert update_task is not None
    assert update_task.status is True


# 5. Teste de validação de dados
def test_task_name_required(client):
    new_task = TaskModel(name=None)

    try:
        db.session.add(new_task)
        db.session.commit()
        assert False, "O commit deveria ter falhado por causa do nome nulo"
    except Exception as e:
        db.session.rollback()
        assert "Integrity" in str(e.__class__.__name__)


# 6. Teste de seleção por id
def test_query_by_id(client):
    new_task = TaskModel(name="Task by ID")

    db.session.add(new_task)
    db.session.commit()

    task = db.session.get(TaskModel, new_task.id)

    assert task is not None
    assert task.id == new_task.id
    assert task.name == "Task by ID"


# 7. Teste de Listagem de Tarefas
def test_task_list(client):
    task1 = TaskModel(name="Task 1")
    task2 = TaskModel(name="Task 2")

    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()

    tasks = TaskModel.query.all()

    assert len(tasks) == 2


# 8. Testes de erro de transação
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
