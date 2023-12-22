from marshmallow import Schema, fields
from src.core.schemas.role import RoleSchema

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    roles = fields.Nested('RoleSchema', many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)