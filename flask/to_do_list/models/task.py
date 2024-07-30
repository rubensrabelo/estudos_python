from datetime import datetime, timezone

from db import db


class Task(db.Model):
    __tablename__ = "tb_task"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    status = db.Column(db.Integer, unique=False, nullable=True)
    create_at = db.Column(
        db.DateTime, nullable=False,
        default=lambda: datetime.now(tz=timezone.utc)
        )
    update_at = db.Column(
        db.DateTime, nullable=False,
        default=lambda: datetime.now(tz=timezone.utc),
        onupdate=lambda: datetime.now(tz=timezone.utc)
        )
