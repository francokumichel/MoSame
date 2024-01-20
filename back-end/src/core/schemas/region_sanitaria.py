from marshmallow import Schema, fields

class RegionSanitariaSchema(Schema):
    tipo = fields.Str()

identidad_genero_schema = RegionSanitariaSchema()
