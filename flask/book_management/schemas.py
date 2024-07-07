from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    pages_quantity = fields.Float(required=True)
    author = fields.Str()
    publishing_company = fields.Str()


class BookUpdateSchema(Schema):
    name = fields.Str()
    pages_quantity = fields.Float()
    author = fields.Str()
    publishing_company = fields.Str()
