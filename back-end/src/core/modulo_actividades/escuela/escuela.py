from src.core.database import db
import enum

class Sectores(enum.Enum):
    ESTATAL = "Estatal"
    PRIVADO = "Privado"

escuela_nivel = db.Table('escuela_nivel',   
    db.Column('escuela_cue', db.String(30), db.ForeignKey('escuela.cue'), primary_key=True),
    db.Column('nivel_nombre', db.String(100), db.ForeignKey('nivel.nombre'), primary_key=True)                                
)

class Escuela(db.Model):
    __tablename__ = "escuela"

    cue = db.Column(db.String(30), primary_key=True)
    nombre = db.Column(db.String(200))
    sector = db.Column(db.String(100))
    niveles = db.relationship("Nivel", secondary=escuela_nivel, backref="escuela")
    modalidad = db.Column(db.String(100))
    municipio_id = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    actividades = db.relationship("Actividad", backref="escuela")