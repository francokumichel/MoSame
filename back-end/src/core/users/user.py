from src.core.database import db
from src.core.permissions import role
from werkzeug.security import generate_password_hash, check_password_hash

users_roles = db.Table(
    "users_roles",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
)

class User(db.Model):
    """Clase que representa un usuario del sistema"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=False)
    last_name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(256))
    roles = db.relationship("Role", secondary=users_roles, backref="users")
    derivaciones = db.relationship("Derivacion", backref="usuario")
    llamadas_cetecsm = db.relationship("LlamadaCetecsm", backref="usuario")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == "password":
                self.set_password(kwargs["password"])
            else:
                setattr(self, key, value)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key == "password":
                self.set_password(kwargs["password"])
            else:
                setattr(self, key, value)