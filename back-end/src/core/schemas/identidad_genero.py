from marshmallow import Schema, fields

class IdentidadGeneroSchema(Schema):
    tipo = fields.Str()
    otro_tipo = fields.Str()

identidad_genero_schema = IdentidadGeneroSchema()
identidades_genero_schema = IdentidadGeneroSchema(many=True)