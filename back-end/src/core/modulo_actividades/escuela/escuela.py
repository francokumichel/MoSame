from src.core.database import db
import enum

class Sectores(enum.Enum):
    ESTATAL = "Estatal"
    PRIVADO = "Privado"

class Escuela(db.Model):
    __tablename__ = "escuela"

    cue = db.Column(db.String(30), primary_key=True)
    nombre = db.Column(db.String(200))
    sector = db.Column(db.String(100))
    niveles = db.Column(db.Text)
    modalidad = db.Column(db.String(100))
    municipio_id = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    actividades = db.relationship("Actividad", backref="escuela")