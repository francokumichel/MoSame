from marshmallow import Schema, fields
from src.core.schemas.escuela import EscuelaSchema
from src.core.schemas.anio import AnioSchema

class ActividadSchema(Schema):
    cant_participantes = fields.Int()
    observaciones = fields.Str()
    cant_encuentros = fields.Int()
    escuela = fields.Nested(EscuelaSchema)
    anios = fields.Nested(AnioSchema, many=True)
    actividad = fields.Str()

actividad_schema = ActividadSchema()
actividades_schema = ActividadSchema(many=True)