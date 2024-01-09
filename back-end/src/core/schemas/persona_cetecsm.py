from marshmallow import Schema, fields
from src.core.schemas.derivacion import DerivacionSchema

class PersonaCetecsmSchema(Schema):
    id = fields.Int(dump_only=True)
    dni = fields.Str()
    grupo_conviviente = fields.Str()
    dio_consentimiento = fields.Bool()
    localidad = fields.Str()
    tiene_obra_social = fields.Bool()
    nombre = fields.Str()
    apellido = fields.Str()
    edad = fields.Int()
    telefono = fields.Str()
    telefono_alternativo = fields.Str()
    fecha_prox_llamado_actual = fields.Date()
    derivacion = fields.Nested(DerivacionSchema)

personas_cetecsm_schemas = PersonaCetecsmSchema(many=True)