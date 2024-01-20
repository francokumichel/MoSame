from marshmallow import Schema, fields

class SituacionVulnerabilidadSchema(Schema):
    tipo = fields.Str()

situacion_vuln_schema = SituacionVulnerabilidadSchema()
situaciones_vuln_schema = SituacionVulnerabilidadSchema(many=True)