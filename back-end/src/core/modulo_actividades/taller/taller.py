from datetime import datetime
import enum
from src.core.database import db
from src.core.modulo_actividades.dispositivo import dispositivo

class TiposActividades(enum.Enum):
    TALLERES = "Talleres de Salud Mental en las Escuelas"
    ESPACIO_GRUPAL = "Espacio Grupal en el Dispositivo"
    ACCIONES_PROMOCION = "Acciones de Promoción y Prevención en la Comunidad"

class Taller(db.Model):
    __tablename__ = "taller"

    id = db.Column(db.Integer, primary_key=True)
    fecha_hora_carga = db.Column(db.Date, default=datetime.now())
    tipo = db.Column(db.String(100), nullable=False)
    municipio_id = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    localidad = db.Column(db.String(100))
    dispositivo_id = db.Column(db.String(100), db.ForeignKey('dispositivo.nombre'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    actividad = db.relationship('Actividad', backref="taller", uselist=False)

