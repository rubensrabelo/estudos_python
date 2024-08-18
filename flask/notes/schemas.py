from marshmallow import Schema, fields


class PlainNoteSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    create_at = fields.DateTime(dump_only=True)
    update_at = fields.DateTime(dump_only=True)


class NoteUpdateSchema(Schema):
    title = fields.Str()
    description = fields.Str()


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class TagUpdateSchema(Schema):
    name = fields.Str(required=True)


class NotesSchema(PlainNoteSchema):
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    notes = fields.List(fields.Nested(PlainNoteSchema()), dump_only=True)


class NotesTagsSchema(Schema):
    id = fields.Int(dump_only=True)
    note_id = fields.Int(dump_only=True)
    tag_id = fields.Int(dump_only=True)
