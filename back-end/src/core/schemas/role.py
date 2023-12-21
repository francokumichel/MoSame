from marshmallow import Schema, fields

class RoleSchema(Schema):
    name = fields.Str()

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)
