from marshmallow import Schema, fields
from src.core.schemas.derivacion import DerivacionSchema
from src.core.schemas.motivo_general_acompanamiento import MotivoGralAcompSchema
from src.core.schemas.identidad_genero import IdentidadGeneroSchema
from src.core.schemas.situacion_vulnerabilidad import SituacionVulnerabilidadSchema
from src.core.schemas.municipio import MunicipioSchema

class Llamada0800Schema(Schema):
    id = fields.Int(dump_only=True)
    telefonos = fields.Str()
    nombre = fields.Str()
    apellido = fields.Str()
    dni = fields.Str()
    municipio_nombre = fields.Str()
    edad = fields.Int()
    definicion = fields.Str()
    detalle_intervencion = fields.Str()
    identidad_genero_tipo = fields.Str()
    pronombre = fields.Str()

llamada_0800_schema = Llamada0800Schema()
llamadas_0800_schema = Llamada0800Schema(many=True)