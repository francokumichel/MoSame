from marshmallow import Schema, fields

class DispositivoSchema(Schema):
    nombre = fields.Str()

dispositivo_schema = DispositivoSchema()
dispositivos_schema = DispositivoSchema(many=True)