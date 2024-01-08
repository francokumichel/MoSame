from marshmallow import Schema, fields

class MotivoGralDerSchema(Schema):
    tipo = fields.Str()

mot_gral_deriv_schema = MotivoGralDerSchema()
mot_grales_deriv_schema = MotivoGralDerSchema(many=True)