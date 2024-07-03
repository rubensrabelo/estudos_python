from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlachemy.exc import SQLAlchemyError

from models import BookModel
from schemas import BookSchema, BookUpdateSchema

blp = Blueprint("Books", __name__, description="Operations on book")


class Item(MethodView):
    def get(self):
        ...

    def post(self):
        ...

    def delete(self):
        ...

    def put(self):
        ...


class ItemModel(MethodView):
    def get(self):
        ...
