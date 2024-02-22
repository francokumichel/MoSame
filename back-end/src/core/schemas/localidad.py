from marshmallow import Schema, fields

class LocalidadSchema(Schema):
    nombre = fields.Str()

localidad_schema = LocalidadSchema()
localidades_schema = LocalidadSchema(many=True)
