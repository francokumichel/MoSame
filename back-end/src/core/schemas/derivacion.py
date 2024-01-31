from marshmallow import Schema, fields
from src.core.schemas.motivo_general_derivacion import MotivoGralDerSchema

class DerivacionSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha = fields.Date()
    dispositivo_derivacion = fields.Str()
    nombre_operador_derivador = fields.Str()
    descripcion = fields.Str()
    mot_gral_derivacion = fields.Nested(MotivoGralDerSchema)

class DerivacionExportarSchema(Schema):
    fecha = fields.Date()
    dispositivo_derivacion = fields.Str()
    nombre_operador_derivador = fields.Str()
    descripcion = fields.Str()


derivacion_schema = DerivacionSchema()