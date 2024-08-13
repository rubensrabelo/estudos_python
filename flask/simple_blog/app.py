from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

import Model

from resources.post import blp as PostBlueprint 


def create_app(db_url=None):
    app = Flask(__name__)

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    return app
