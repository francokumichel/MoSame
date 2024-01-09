from src.core.database import db
from src.core.situaciones_vulnerabilidad import situacion_vulnerabilidad
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

llamcetecsm_sit_vuln = db.Table('llamcetecsm_sit_vul', 
    db.Column('llamada_cetecsm_id', db.Integer, db.ForeignKey('llamada_cetecsm.id'), primary_key=True),
    db.Column('sit_vuln_id', db.String(100), db.ForeignKey('situaciones_vulnerabilidad.tipo', primary_key=True))                                
)

class LlamadaCetecsm(db.Model):
    __tablename__ = "llamada_cetecsm"
    
    id = db.Column(db.Integer, primary_key=True)
    situaciones_vulnerabilidad = db.relationship('SituacionVulnerabilidad', secondary=llamcetecsm_sit_vuln, backref="llamadas_cetecsm")
    detalle_acompanamiento = db.Column(db.String(256))
    detalle = db.Column(db.String(256))
    resolucion = db.Column(db.String(100))
    fecha_llamado = db.Column(db.Date, default=func.current_date())
    fecha_prox_llamado = db.Column(db.Date)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    persona_cetecsm_id = db.Column(db.Integer, db.ForeignKey('persona_cetecsm.id'), nullable=False)
    motivo_gral_acomp_id = db.Column(db.String(100), db.ForeignKey("motivo_general_acompanamiento.tipo"))   