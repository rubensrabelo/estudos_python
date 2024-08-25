from datetime import datetime

from db import db


class TaskModel(db.Model):
    __tablename__ = "tb_tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(
        db.DateTime, nullable=False,
        default=datetime.now
    )
    updated_at = db.Column(
        db.DateTime, nullable=False,
        default=datetime.now,
        onupdate=datetime.now
    )
