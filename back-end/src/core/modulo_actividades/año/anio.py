from src.core.database import db
import enum

anio_division = db.Table('anio_division',   
    db.Column('anio_id', db.Integer, db.ForeignKey('anio.id'), primary_key=True),
    db.Column('division_id', db.String(5), db.ForeignKey('division.nombre'), primary_key=True)                                
)

class Anios(enum.Enum):
    PRIMERO = "1ro"
    SEGUNDO = "2do"
    TERCERO = "3ro"
    CUARTO = "4to"
    QUINTO = "5to"
    SEXTO = "6to"
    SEPTIMO = "7mo"

class Anio(db.Model):
    __tablename__ = "anio"

    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String(5))
    divisiones = db.relationship("Division", secondary=anio_division, backref="anios")

