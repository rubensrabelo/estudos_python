from db import db


class NotesTags(db.Model):
    __tablename__ = "tb_notes_tags"

    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey("tb_notes.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tb_tags.id"))
