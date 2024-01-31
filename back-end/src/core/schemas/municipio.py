from marshmallow import Schema, fields
from src.core.schemas.region_sanitaria import RegionSanitariaSchema
from src.core.schemas.localidad import LocalidadSchema

class MunicipioSchema(Schema):
    nombre = fields.Str()
    region_sanitaria = fields.Nested(RegionSanitariaSchema)
    localidades = fields.Nested(LocalidadSchema, many=True)

municipio_schema = MunicipioSchema()
municipios_schema = MunicipioSchema(many=True)