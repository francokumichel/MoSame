from marshmallow import Schema, fields
from src.core.schemas.region_sanitaria import RegionSanitariaSchema

class MunicipioSchema(Schema):
    nombre = fields.Str()
    region_sanitaria = fields.Nested(RegionSanitariaSchema)

municipio_schema = MunicipioSchema()
municipios_schema = MunicipioSchema(many=True)