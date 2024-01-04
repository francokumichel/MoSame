from marshmallow import Schema, fields


class MalestarEmocionalSchema(Schema):
    tipo = fields.Str()