from src.core.database import db
import enum
from sqlalchemy import func

class MotivoDeLaConsulta(enum.Enum):
    ASISTENCIA = "Asistencia en Salud Mental"
    ORIENTACION = "Orientación en Salud Mental"
    OTROS = "Otros"

class SujetoDeLaConsulta(enum.Enum):
    PROPIA = "Propia"
    TERCERO = "Tercero"

class Pronombre(enum.Enum):
    EL = "Él"
    ELLA = "Ella"
    ELLE = "Elle"

class Llamada0800(db.Model):
    __tablename__ = "llamada_0800"

    id = db.Column(db.Integer, primary_key=True)
    motivo = db.Column(db.String(100))
    como_ubico = db.Column(db.String(256))
    municipio_id = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    sujeto = db.Column(db.String(15))
    edad = db.Column(db.Integer)
    identidad_genero_id = db.Column(db.String(100), db.ForeignKey('identidad_genero.tipo'))
    pronombre = db.Column(db.String(5))
    grupo_conviviente = db.Column(db.String(50))
    grupo_conviviente_otro = db.Column(db.String(50)) # TODO

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