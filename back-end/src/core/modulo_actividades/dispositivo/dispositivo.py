from src.core.database import db

class Dispositivo(db.Model):
    __tablename__ = "dispositivo"

    nombre = db.Column(db.String(100), primary_key=True)