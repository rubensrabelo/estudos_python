from marshmallow import Schema, fields


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    country = fields.Str()


class AuthorUpdateSchema(Schema):
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    country = fields.Str()


class PlainBookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    pages_qtd = fields.Str(required=True)
    price = fields.Float(required=True)
    publishing_company = fields.Str()
    country = fields.Str()


class BookSchema(PlainBookSchema):
    author_id = fields.Int(required=True, load_only=True)
    author = fields.List(fields.Nested(AuthorSchema()), dump_only=True)


class BookUpdateSchema(PlainBookSchema):
    ...
