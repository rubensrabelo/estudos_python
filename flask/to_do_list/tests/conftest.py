import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from app import create_app
from db import db
from models.task import TaskModel

@pytest.fixture(scope="module")
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


@pytest.fixture(scope="module")
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(autouse=True)
def clean_db():
    db.session.query(TaskModel).delete()
    db.session.commit()
