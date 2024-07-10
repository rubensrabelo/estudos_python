from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import AuthorModel
from schemas import AuthorSchema, AuthorUpdateSchema

blp = Blueprint("Authors", __name__, description="Operations of authors")


@blp.route("/authors/<string:author_id>")
class Author(MethodView):
    @blp.response(200, AuthorSchema)
    def get(self, author_id):
        author = AuthorModel.query.get_or_404(author_id)
        return author

    @blp.arguments(AuthorUpdateSchema)
    @blp.response(200, AuthorSchema)
    def put(self, author_data, author_id):
        author = AuthorModel.query.get(author_id)
        if author:
            author.full_name = author_data["full_name"]
            author.gender = author_data["gender"]
            author.country = author_data["country"]
        else:
            author = AuthorModel(id=author_id, **author_data)
        db.session.add(author)
        db.session.commit()
        return author

    def delete(self, author_id):
        author = AuthorModel.query.get_or_404(author_id)
        db.session.delete(author)
        db.session.commit()
        return {"message": "Author deleted"}


@blp.route("/authors")
class AuthorList(MethodView):
    @blp.response(200, AuthorSchema(many=True))
    def get(self):
        return AuthorModel.query.all()

    @blp.arguments(AuthorSchema)
    @blp.response(201, AuthorSchema)
    def post(self, author_data):
        author = AuthorModel(**author_data)
        try:
            db.session.add(author)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A author with that full name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the author.")
        return author
