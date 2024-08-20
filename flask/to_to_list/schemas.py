from marshmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    name = fields.Bool()
    create_at = fields.DateTime(dump_only=True)
    update_at = fields.DateTime(dump_only=True)


class TaskUpdateSchema(Schema):
    name = fields.Str(required=True)
    name = fields.Bool()
