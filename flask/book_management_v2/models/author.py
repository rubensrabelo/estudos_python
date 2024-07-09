from db import db


class AuthorModel(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    country = db.Column(db.String(20), unique=False, nullable=True)
