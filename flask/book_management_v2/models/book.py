from db import db


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    pages_qtd = db.Column(db.Integer, unique=False, nullable=True)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    publishing_company = db.Column(db.String(80), unique=False, nullable=True)
    country = db.Column(db.String(20), unique=False, nullable=True)

    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
