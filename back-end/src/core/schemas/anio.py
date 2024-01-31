from marshmallow import Schema, fields
from src.core.schemas.division import DivisionSchema

class AnioSchema(Schema):
    anio = fields.Str()
    divisiones = fields.Nested(DivisionSchema, many=True)

anio_schema = AnioSchema()
anios_schema = AnioSchema(many=True)