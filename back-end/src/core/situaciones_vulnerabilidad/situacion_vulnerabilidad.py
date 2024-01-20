from src.core.database import db

class SituacionVulnerabilidad(db.Model):
    """ Clase que representa el modelo de los tipos de situaciones de vulnerabilidad que hay """
    __tablename__ = "situaciones_vulnerabilidad"

    tipo = db.Column(db.String(100), primary_key=True)