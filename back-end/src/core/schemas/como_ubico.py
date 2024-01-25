from marshmallow import Schema, fields

class ComoUbicoSchema(Schema):
    forma = fields.Str()

como_ubico_schema = ComoUbicoSchema()
como_ubico_schema_many = ComoUbicoSchema(many=True)