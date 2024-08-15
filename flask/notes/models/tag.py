from db import db


class TagModel(db.Model):
    __tablename__ = "tb_tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
