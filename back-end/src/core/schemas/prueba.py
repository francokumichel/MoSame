from marshmallow import Schema, fields


class PruebaSchema(Schema):
    name = fields.Str()