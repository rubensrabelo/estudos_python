from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import BookModel
from schemas import BookSchema, BookUpdateSchema

blp = Blueprint("Books", __name__, description="Operations on book")


@blp.route("/books/<string:book_id>")
class Book(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        book = BookModel.query.get_or_404(book_id)
        return book

    @blp.arguments(BookUpdateSchema)
    @blp.response(200, BookSchema)
    def put(self, book_data, book_id):
        book = BookModel.query.get(book_id)

        if book:
            book.title = book_data["title"]
            book.pages_qtd = book_data["pages_qtd"]
            book.price = book_data["price"]
            book.publishing_company = book_data["publishing_company"]
            book.country = book_data["country"]
            book.author_id = book_data["author_id"]
        else:
            book = BookModel(id=book_id, **book_data)
        db.session.add(book)
        db.session.commit()
        return book

    def delete(self, book_id):
        book = BookModel.query.get_or_404(book_id)

        db.session.delete(book)
        db.session.commit()
        return {"message": "Book deleted."}


@blp.route("/books")
class BookList(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return BookModel.query.all()

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, book_data):
        book = BookModel(**book_data)
        try:
            db.session.add(book)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A book with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the author.")
        return book
