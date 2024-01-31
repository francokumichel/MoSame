from datetime import datetime
from src.core.database import db
from src.core.modulo_actividades.dispositivo import dispositivo

class Taller(db.Model):
    __tablename__ = "taller"

    id = db.Column(db.Integer, primary_key=True)
    fecha_hora_carga = db.Column(db.Date, default=datetime.now())
    municipio_id = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    localidad_id = db.Column(db.String(100), db.ForeignKey('localidad.nombre'))
    dispositivo_id = db.Column(db.String(100), db.ForeignKey('dispositivo.nombre'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    actividad = db.relationship('Actividad', backref="taller", uselist=False)

