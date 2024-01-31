from marshmallow import Schema, fields
from src.core.schemas.actividad import ActividadSchema

class TallerSchema(Schema):
    fecha_hora_carga = fields.Date()
    municipio_id = fields.Str()
    localidad_id = fields.Str()
    dispositivo_id = fields.Str()
    actividad = fields.Nested(ActividadSchema)

taller_schema = TallerSchema()
talleres_schema = TallerSchema(many=True)