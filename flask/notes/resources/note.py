from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import NoteModel
from schemas import NoteSchema, NoteUpdateSchema

blp = Blueprint("Notes", __name__)


@blp.route("/notes/<string:note_id>")
class Note(MethodView):
    @blp.response(200, NoteSchema)
    def get(self, note_id):
        note = NoteModel.query.get_or_404(note_id)

        return note

    def delete(self, note_id):
        note = NoteModel.query.get_or_404(note_id)

        db.session.delete(note)
        db.session.commit()

        return {"message": "Note deleted."}

    @blp.arguments(NoteUpdateSchema)
    @blp.response(200, NoteSchema)
    def put(self, note_data, note_id):
        note = NoteModel.query.get(note_id)

        if note:
            note.title = note_data["title"]
            note.description = note_data["description"]
        else:
            note = NoteModel(id=note_id, **note_data)

        db.session.add(note)
        db.session.comit()

        return note


@blp.route("/notes")
class NoteList(MethodView):
    @blp.response(200, NoteSchema(many=True))
    def get(self):
        return NoteModel.query.all()

    @blp.arguments(NoteSchema)
    @blp.response(201, NoteSchema)
    def post(self, note_data):
        note = NoteModel(**note_data)

        try:
            db.session.add(note)
            db.session.commit()
        except SQLAlchemyError:
            abort(
                500, message="An error occurred while inserting the item."
            )
