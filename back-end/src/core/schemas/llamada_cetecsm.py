from marshmallow import fields, Schema

class LlamadaCetecsmSchema(Schema):
    id = fields.Int(dump_only=True)
    detalle = fields.Str()
    resolucion = fields.Str()
    fecha_llamado = fields.Date()
    fecha_prox_llamado = fields.Date()

llamada_cetecsm_schema = LlamadaCetecsmSchema()
llamadas_cetecsm_schema = LlamadaCetecsmSchema(many=True)