from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlachemy.exc import SQLAlchemyError

from db import db
from models import BookModel
from schemas import BookSchema, BookUpdateSchema

blp = Blueprint("Books", __name__, description="Operations on book")


@blp.route("/book/<string:book_id>")
class Book(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        book = BookModel.query.get_or_404(book_id)
        return book

    def delete(self, book_id):
        book = BookModel.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return {"message": "Book deleted."}

    @blp.arguments(BookUpdateSchema)
    @blp.response(200, BookSchema)
    def put(self, book_data, book_id):
        book = BookModel.query.get(book_id)

        if book:
            book["name"] = book_data["name"]
            book["pages_quantity"] = book_data["pages_quantity"]
            book["author"] = book_data["author"]
            book["publishing_company"] = book_data["publishing_company"]
        else:
            book = BookModel(id=book_id, **book_data)

        db.session.add(book)
        db.session.commit()

        return book


@blp.route("/book")
class BookList(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return BookModel.query.all()

    def post(self):
        ...
