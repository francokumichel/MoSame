from marshmallow import Schema, fields
from src.core.schemas.derivacion import DerivacionSchema
from src.core.schemas.motivo_general_acompanamiento import MotivoGralAcompSchema
from src.core.schemas.identidad_genero import IdentidadGeneroSchema
from src.core.schemas.situacion_vulnerabilidad import SituacionVulnerabilidadSchema
from src.core.schemas.municipio import MunicipioSchema

class PersonaCetecsmSchema(Schema):
    id = fields.Int(dump_only=True)
    dni = fields.Str()
    grupo_conviviente = fields.Str()
    grupo_conviviente_otro = fields.Str()
    dio_consentimiento = fields.Bool()
    esta_asignada = fields.Bool()
    localidad = fields.Str()
    tiene_obra_social = fields.Bool()
    obra_social = fields.Str()
    nombre = fields.Str()
    apellido = fields.Str()
    edad = fields.Int()
    telefono = fields.Str()
    telefono_alternativo = fields.Str()
    fecha_prox_llamado_actual = fields.Date()
    detalle_acompanamiento = fields.Str()
    municipio = fields.Nested(MunicipioSchema)
    derivacion = fields.Nested(DerivacionSchema)
    motivo_gral_acomp = fields.Nested(MotivoGralAcompSchema)
    identidad_genero = fields.Nested(IdentidadGeneroSchema)
    situaciones_vulnerabilidad = fields.Nested(SituacionVulnerabilidadSchema, many=True)

persona_cetecsm_schemas = PersonaCetecsmSchema()
personas_cetecsm_schemas = PersonaCetecsmSchema(many=True)