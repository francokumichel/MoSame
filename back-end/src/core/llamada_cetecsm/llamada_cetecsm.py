from src.core.database import db
import enum
from sqlalchemy import func

class ResolucionLlamado(enum.Enum):
    EN_PRIMER_LLAMADO = "Se resolvió en el primer llamado"
    RECHAZA = "Rechaza acompañamiento"
    CONTINUA = "Continua acompañamiento"
    FALLIDA = "Comunicación fallida"
    FALLO_COMUNICACION = "Fin de acompañamiento por fallo en la comunicación"
    DERIVACION = "Fin de acompañamiento por derivación a territorio"
    RESOLUCION = "Fin del acompañamiento por resolución"

class LlamadaCetecsm(db.Model):
    __tablename__ = "llamada_cetecsm"
    
    id = db.Column(db.Integer, primary_key=True)
    detalle = db.Column(db.String(256))
    resolucion = db.Column(db.String(100))
    fecha_llamado = db.Column(db.Date, default=func.current_date())
    fecha_prox_llamado = db.Column(db.Date)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    persona_cetecsm_id = db.Column(db.Integer, db.ForeignKey('persona_cetecsm.id'), nullable=False)   