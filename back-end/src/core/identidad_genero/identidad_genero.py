from src.core.database import db

class IdentidadGenero(db.Model):
    """ Clase que representa el modelo de identidades de genero """
    __tablename__ = "identidad_genero"

    tipo = db.Column(db.String(100), primary_key=True)
    personas_cetecsm = db.relationship("PersonaCetecsm", backref="identidad_genero")