from flask.view import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exe import SQLAlchemyError, IntegrityError

from db import db
from models import TagsModel
from schemas import TagSchema, TagUpdateSchema

blp = Blueprint("Tags", __name__)


class Tag(MethodView):
    ...
