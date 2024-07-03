from db import db


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    pages_quantity = db.Column(db.Float(precision=2), unique=False, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=True)
    publishing_company = db.Column(db.String(80), unique=False, nullable=True)
