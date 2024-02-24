from marshmallow import Schema, fields
from src.core.schemas.derivacion import DerivacionSchema, DerivacionExportarSchema
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
    fecha_ultimo_llamado = fields.Date()
    detalle_acompanamiento = fields.Str()
    municipio = fields.Nested(MunicipioSchema)
    derivacion = fields.Nested(DerivacionSchema)
    motivo_gral_acomp_id = fields.Str()
    malestares_emocionales = fields.Str()
    identidad_genero_id = fields.Str()
    identidad_genero_otra = fields.Str()
    situaciones_vulnerabilidad = fields.Str()

persona_cetecsm_schemas = PersonaCetecsmSchema()
personas_cetecsm_schemas = PersonaCetecsmSchema(many=True)

class PersonaCetecsmExportarSchema(Schema):
    dio_consentimiento = fields.Bool()
    municipio_id = fields.Str()
    nombre = fields.Str()
    apellido = fields.Str()
    edad = fields.Int()
    dni = fields.Str()
    telefono = fields.Str()
    telefono_alternativo = fields.Str()
    grupo_conviviente = fields.Str()
    localidad = fields.Str()
    identidad_genero_id = fields.Str()
    obra_social = fields.Str()
    detalle_acompanamiento = fields.Str()
    fecha_prox_llamado_actual = fields.Date()
    motivo_gral_acomp = fields.Nested(MotivoGralAcompSchema)
    derivacion = fields.Nested(DerivacionExportarSchema)

personas_cetecsm_exportar_schemas = PersonaCetecsmExportarSchema(many=True)