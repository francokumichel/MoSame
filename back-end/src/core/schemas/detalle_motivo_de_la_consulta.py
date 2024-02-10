from marshmallow import Schema, fields

class DetalleMotivoDeLaConsultaSchema(Schema):
    motivo = fields.Str()

detalle_motivo_de_la_consulta_schema = DetalleMotivoDeLaConsultaSchema()
detalle_motivos_de_la_consulta_schema = DetalleMotivoDeLaConsultaSchema(many=True)