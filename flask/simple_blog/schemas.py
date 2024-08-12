from marshmallow import Schema, fields


class PostSchema(Schema):
    id = fields.Integer(dumpy_only=True)
    title = fields.String(required=True)
    comment = fields.String(required=True)
    create_at = fields.DateTime(dumpy_only=True)
    update_at = fields.DateTime(dumpy_only=True)


class PostUpdateSchema(Schema):
    title = fields.String()
    comment = fields.String()
