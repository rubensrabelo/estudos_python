import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from app import create_app
from db import db
from models.task import TaskModel


def pytest_addoption(parser):
    parser.addoption(
        "--test-type", action="store", 
        default="unit", help="Specify test type: unit or integration"
        )


@pytest.fixture(scope="session")
def app(request):
    test_type = request.config.getoption("--test-type")

    if test_type == "integration":
        app = create_app("integration")
    else:
        app = create_app("testing")

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="module")
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope="function", autouse=True)
def clean_db():
    db.session.query(TaskModel).delete()
    db.session.commit()
