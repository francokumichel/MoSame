from marshmallow import Schema, fields

class DivisionSchema(Schema):
    nombre = fields.Str()

division_schema = DivisionSchema()
divisiones_schema = DivisionSchema(many=True)