from src.core.database import db

class Localidad(db.Model):
    __tablename__ = "localidad"

    nombre = db.Column(db.String(100), primary_key=True)
    talleres = db.relationship("Taller", backref="localidad")