from src.core.database import db
from src.core.general.localidad import localidad
from src.core.modulo_actividades.taller import taller

class Municipio(db.Model):
    __tablename__ = "municipio"
    nombre = db.Column(db.String(100), primary_key=True)
    region_sanitaria_id = db.Column(db.String(50), db.ForeignKey('region_sanitaria.tipo'))
    personas_cetecsm = db.relationship("PersonaCetecsm", backref="municipio")
    talleres = db.relationship("Taller", backref="municipio")
    localidades = db.Column(db.Text)