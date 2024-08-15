from db import db


class NoteTag(db.Model):
    __tablename__ = "tb_note_tag"

    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey("tb_notes.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tb_tags.id"))
