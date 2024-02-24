from marshmallow import Schema, fields
from src.core.schemas.actividad import ActividadSchema
from src.core.schemas.municipio import MunicipioSchema

class TallerSchema(Schema):
    tipo = fields.Str()
    fecha_hora_carga = fields.Date()
    municipio = fields.Nested(MunicipioSchema)
    localidad = fields.Str()
    dispositivo_id = fields.Str()
    actividad = fields.Nested(ActividadSchema)

taller_schema = TallerSchema()
talleres_schema = TallerSchema(many=True)