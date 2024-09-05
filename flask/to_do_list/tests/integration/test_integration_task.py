import pytest

from db import db
from models.task import TaskModel


def test_simple_request(client):
    response = client.get("/tasks")
    assert response.status_code == 200
