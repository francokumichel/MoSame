from marshmallow import Schema, fields


class ActividadExternaSchema(Schema):
    nombre = fields.Str()

actividad_externa_schema = ActividadExternaSchema()
actividades_externas_schema = ActividadExternaSchema(many=True)