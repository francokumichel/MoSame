from marshmallow import Schema, fields
from src.core.schemas.derivacion import DerivacionSchema
from src.core.schemas.motivo_general_acompanamiento import MotivoGralAcompSchema
from src.core.schemas.situacion_vulnerabilidad import SituacionVulnerabilidadSchema

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
    detalle_acompanamiento = fields.Str()
    derivacion = fields.Nested(DerivacionSchema)
    motivo_gral_acomp = fields.Nested(MotivoGralAcompSchema)
    situaciones_vulnerabilidad = fields.Nested(SituacionVulnerabilidadSchema, many=True)

persona_cetecsm_schemas = PersonaCetecsmSchema()
personas_cetecsm_schemas = PersonaCetecsmSchema(many=True)