from marshmallow import Schema, fields
from src.core.schemas.nivel import NivelSchema

class EscuelaSchema(Schema):
    cue = fields.Str()
    nombre = fields.Str()
    sector = fields.Str()
    niveles = fields.Nested(NivelSchema, many=True)
    modalidad = fields.Str()
    