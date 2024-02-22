from marshmallow import Schema, fields


class ActividadInternaSchema(Schema):
    nombre = fields.Str()

actividad_interna_schema = ActividadInternaSchema()
actividades_internas_schema = ActividadInternaSchema(many=True)