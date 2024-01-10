from marshmallow import Schema, fields
from src.core.schemas.malestar_emocional import MalestarEmocionalSchema

class MotivoGralAcompSchema(Schema):
    tipo = fields.Str()
    malestares_emocionales = fields.Nested(MalestarEmocionalSchema, many=True)

mot_gral_acomp_schema = MotivoGralAcompSchema()
mot_grales_acomp_schema = MotivoGralAcompSchema(many=True)