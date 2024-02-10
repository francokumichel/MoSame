from marshmallow import Schema, fields

class MotivoDeLaConsultaSchema(Schema):
    nombre = fields.Str()

motivo_de_la_consulta_schema = MotivoDeLaConsultaSchema()
motivos_de_la_consulta_schema = MotivoDeLaConsultaSchema(many=True)