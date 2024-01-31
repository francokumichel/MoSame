from marshmallow import Schema, fields

class DispositivoSchema(Schema):
    anio = fields.Str()

dispositivo_schema = DispositivoSchema()
dispositivos_schema = DispositivoSchema(many=True)