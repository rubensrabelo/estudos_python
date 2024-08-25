import pymysql
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv

import models
from db import db
from resources.task import blp as TaskBlueprint
from config import Config


pymysql.install_as_MySQLdb()


def create_app(db_url=None):
    app = Flask(__name__)

    load_dotenv()

    configure_app(app, db_url)

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.register_blueprint(TaskBlueprint)

    return app


def configure_app(app, db_url):
    app.config.from_object(Config)

    if db_url:
        app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = Config.get_db_url()
