from marshmallow import Schema, fields
from src.core.schemas.malestar_emocional import MalestarEmocionalSchema

class MotivoGralDerSchema(Schema):
    tipo = fields.Str()
    malestares_emocionales = fields.Nested(MalestarEmocionalSchema, many=True)

mot_gral_deriv_schema = MotivoGralDerSchema()