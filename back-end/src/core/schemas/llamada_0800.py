import json
from marshmallow import Schema, fields, post_dump
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

    @post_dump
    def cambiar_formato_telefonos(self, data, **kwargs):
        if (data['telefonos'] != ''):
            telefonos = json.loads(data['telefonos'])
            telefonos_str = ''
            for telefono in telefonos:
                telefonos_str += telefono['numero'] + ', '
            telefonos_str = telefonos_str[:-2]
            data['telefonos'] = telefonos_str

        return data

llamada_0800_schema = Llamada0800Schema()
llamadas_0800_schema = Llamada0800Schema(many=True)
class ObservatorioLlamada0800Schema(Schema):
    fecha_y_hora_carga = fields.Date()
    municipio = fields.Nested(MunicipioSchema)
    identidad_genero_tipo = fields.Str()
    edad = fields.Int()
    demanda_tratamiento = fields.Bool()
    motivo_nombre = fields.Str()
    detalle_motivo_motivo = fields.Str()
    malestares_emocionales = fields.Str()

    @post_dump
    def cambiar_formato_malestares(self, data, **kwargs):
        if (data['malestares_emocionales'] != ''):
            data['malestares_emocionales'] = data['malestares_emocionales'].replace('"', '').replace('[', '').replace(']', '').replace(',', ', ')

        print(data)
        
        return data

observatorio_llamada_0800_schema = ObservatorioLlamada0800Schema()
observatorio_llamadas_0800_schema = ObservatorioLlamada0800Schema(many=True)