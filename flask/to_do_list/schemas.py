from mashmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Int()
    expiration_date = fields.Date() # Ver se está correto essa parte
