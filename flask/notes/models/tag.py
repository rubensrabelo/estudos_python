from db import db


<<<<<<< HEAD
class TagModel(db.Model):
    __tablename__ = "tb_tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
=======
class TagsModel(db.Model):
    __tablename__ = "tb_tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    notes = db.relationship(
        "NoteModel", back_populates="tags", secondary="tb_notes_tags"
        )
>>>>>>> working
