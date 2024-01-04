from src.core.database import db

class Municipio(db.Model):
    """ Clase que representa el modelo de municipios disponibles """
    __tablename__ = "municipio"
    
    nombre = db.Column(db.String(100), primary_key=True)
#    personas_cetecsm = db.relationship("PersonaCetecsm", backref="municipio")