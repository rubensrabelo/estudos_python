from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask.exc import SQLAlchemyError, InterityError

from db import db
from models import BookModel
from schemas import BookSchema, BookUpdateSchema

blp = Blueprint("Books", __name__, description="Operations on book")


class Book(MethodView):
    ...


class BookList(MethodView):
    ...
