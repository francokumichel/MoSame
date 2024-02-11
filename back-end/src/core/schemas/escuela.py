from marshmallow import Schema, fields

class EscuelaSchema(Schema):
    cue = fields.Str()
    nombre = fields.Str()
    sector = fields.Str()
    niveles = fields.Str()
    modalidad = fields.Str()
    