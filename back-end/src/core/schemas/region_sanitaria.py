from marshmallow import Schema, fields

class RegionSanitariaSchema(Schema):
    tipo = fields.Str()

region_sanitaria_schema = RegionSanitariaSchema()
regiones_sanitarias_schema = RegionSanitariaSchema(many=True)
