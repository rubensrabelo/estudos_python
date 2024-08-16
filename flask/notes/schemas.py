from marshmallow import Schema, fields


class PlainNoteSchema(Schema):
    ...


class NotesSchema(PlainNoteSchema):
    ...


class NoteUpdateSchema(Schema):
    ...


class PlainTagSchema(Schema):
    ...


class TagSchema(PlainTagSchema):
    ...


class TagUpdateSchema(Schema):
    ...
