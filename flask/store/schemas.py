from marshmallow import Schema, fields


class StoreSchema(Schema):
    id = fields.Str(dumpy_only=True)
    name = fields.Str(required=True)


class ItemSchema(Schema):
    id = fields.Str(dumpy_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

    store_id = fields.Str(required=True)


class ItemsUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
