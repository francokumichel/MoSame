from marshmallow import Schema, fields

class NivelSchema(Schema):
    nombre = fields.Str()

nivel_schema = NivelSchema()
niveles_schema = NivelSchema(many=True)