import os
import pymysql
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv

import models

from db import db
from resources.task import blp as TaskBlueprint

pymysql.install_as_MySQLdb()


def create_app(db_url=None):
    app = Flask(__name__)

    load_dotenv()

    app.config["API_TITLE"] = "To Do List REST API"
    app.config["API_VERSION"] = "v2"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    if not db_url:
        db_url = (
            f"mysql+pymysql://{os.getenv('DB_USERNAME')}:"
            f"{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST')}:"
            f"{os.getenv('DB_PORT')}/"
            f"{os.getenv('DB_NAME')}"
        )

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.register_blueprint(TaskBlueprint)

    return app
