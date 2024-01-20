from marshmallow import Schema, fields


class MalestarEmocionalSchema(Schema):
    tipo = fields.Str()

malestar_emocional_schema = MalestarEmocionalSchema()
malestares_emocionales_schema = MalestarEmocionalSchema(many=True)