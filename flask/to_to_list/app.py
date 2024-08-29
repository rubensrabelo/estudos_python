import pymysql
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv

import models
from db import db
from resources.task import blp as TaskBlueprint
from config import Config, TestingConfig


pymysql.install_as_MySQLdb()


def create_app(db_url=None):
    app = Flask(__name__)

    load_dotenv()

    if db_url == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(Config)

    configure_app(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.register_blueprint(TaskBlueprint)

    return app


def configure_app(app):
    if app.config.get("SQLALCHEMY_DATABASE_URI") is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = Config.get_db_url()
