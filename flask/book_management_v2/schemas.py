from marshmallow import Schema, fields


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    full_name = fields.Str(required=True)
    gender = fields.Str(required=True)
    country = fields.Str()


class AuthorUpdateSchema(Schema):
    full_name = fields.Str(required=True)
    gender = fields.Str(required=True)
    country = fields.Str()


class PlainBookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    pages_qtd = fields.Int(required=True)
    price = fields.Float(required=True)
    publishing_company = fields.Str()
    country = fields.Str()


class BookSchema(PlainBookSchema):
    author_id = fields.Int(required=True, load_only=True)
    author = fields.List(fields.Nested(AuthorSchema()), dump_only=True)


class BookUpdateSchema(Schema):
    title = fields.Str()
    pages_qtd = fields.Int()
    price = fields.Float()
    publishing_company = fields.Str()
    country = fields.Str()
    author_id = fields.Int()
