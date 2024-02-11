from marshmallow import Schema, fields

class AnioSchema(Schema):
    anio = fields.Str()
    divisiones = fields.Str()

anio_schema = AnioSchema()
anios_schema = AnioSchema(many=True)