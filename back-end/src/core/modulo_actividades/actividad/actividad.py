from src.core.database import db
import enum

actividad_anio = db.Table('actividad_anio',   
    db.Column('actividad_id', db.Integer, db.ForeignKey('actividad.id'), primary_key=True),
    db.Column('anio_id', db.Integer, db.ForeignKey('anio.id'), primary_key=True)                                
)

class Actividad(db.Model):
    __tablename__ = "actividad"

    id = db.Column(db.Integer, primary_key=True)
    taller_id = db.Column(db.Integer, db.ForeignKey('taller.id'))
    cant_participantes = db.Column(db.Integer)
    observaciones = db.Column(db.String(256))
    cant_encuentros = db.Column(db.Integer)
    escuela_cue = db.Column(db.String(30), db.ForeignKey('escuela.cue'))
    anios = db.relationship("Anio", secondary=actividad_anio, backref="actividades")
    actividad = db.Column(db.String(100))
    