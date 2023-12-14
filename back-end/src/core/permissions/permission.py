from src.core.database import db


class Permission(db.Model):
    """Clase que representa el modelo de permisos"""

    __tablename__ = 'permissions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)