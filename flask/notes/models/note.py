from datetime import datetime, timezone

from db import db


class NoteModel(db.Model):
    __tablename__ = "tb_notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String, nullable=True)
    create_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(tz=timezone.utc)
    )
    update_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(tz=timezone.utc),
        onupdate=lambda: datetime.now(tz=timezone.utc)
    )

    tags = db.relationship(
        "TagModel", back_populates="notes", secondary="tb_notes_tags"
        )
