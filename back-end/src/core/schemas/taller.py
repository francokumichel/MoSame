from marshmallow import Schema, fields
from src.core.schemas.actividad import ActividadSchema
from src.core.schemas.municipio import MunicipioSchema
from src.core.schemas.escuela import EscuelaSchema

class TallerSchema(Schema):
    tipo = fields.Str()
    fecha_hora_carga = fields.Date()
    municipio = fields.Nested(MunicipioSchema)
    localidad = fields.Str()
    dispositivo_id = fields.Str()
    actividad = fields.Nested(ActividadSchema)

taller_schema = TallerSchema()
talleres_schema = TallerSchema(many=True)

class TallerSchemaObservatorio(Schema):
    tipo = fields.Str()
    municipio = fields.Nested(MunicipioSchema)
    localidad = fields.Str()
    dispositivo_id = fields.Str()
    actividad = fields.Nested(ActividadSchema)
    escuela = fields.Nested(EscuelaSchema)
    cant_participantes = fields.Int()
    cant_encuentros = fields.Int()

taller_schema_observatorio = TallerSchemaObservatorio()
talleres_schema_observatorio = TallerSchemaObservatorio(many=True)