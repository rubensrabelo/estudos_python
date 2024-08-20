from datetime import datetime, timezone

from db import db


class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    create_at = db.Column(
        db.DateTime, nullable=False,
        default=lambda: datetime.now(tz=timezone.utc)
    )
    update_at = db.Column(
        db.DateTime, nullable=False,
        default=lambda: datetime.now(tz=timezone.utc),
        onupdate=lambda: datetime.now(tz=timezone.utc)
    )
