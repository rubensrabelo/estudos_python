from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    pages_quantity = fields.Float(required=True)
    author = fields.Str()
    publishing_company = fields.Str()
