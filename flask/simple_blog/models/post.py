from datetime import datetime, timezone

from db import db


class PostModel(db.Model):
    __tablename__ = "tb_posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    comment = db.Column(db.String(200), unique=False, nullable=False)
    create_at = db.Column(
        db.DateTime, nullable=False,
        default=lambda: datetime.now(tz=timezone.utc)
        )
    update_at = db.Column(
        db.Datetime, nullable=False,
        default=lambda: datetime.now(tz=timezone.utc),
        onupdate=lambda: datetime.now(tz=timezone.utc)
    )
