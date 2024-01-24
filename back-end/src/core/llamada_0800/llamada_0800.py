from src.core.database import db
import enum
from sqlalchemy import func

class MotivoDeLaConsulta(db.Model):
    __tablename__ = "motivo_consulta"

    nombre = db.Column(db.String(100), primary_key=True)

class ComoUbico(db.Model):
    __tablename__ = "como_ubico"

    forma = db.Column(db.String(100), primary_key=True)

class SujetoDeLaConsulta(enum.Enum):
    PROPIA = "Propia"
    TERCERO = "Tercero"

class Pronombre(enum.Enum):
    EL = "Él"
    ELLA = "Ella"
    ELLE = "Elle"

class DetalleMotivoConsulta(db.Model):
    __tablename__ = "detalle_motivo_consulta"

    motivo = db.Column(db.String(100), primary_key=True)

class Llamada0800(db.Model):
    __tablename__ = "llamada_0800"

    id = db.Column(db.Integer, primary_key=True)
    motivo_id = db.Column(db.String(100), db.ForeignKey("motivo_consulta.nombre"))
    como_ubico_id = db.Column(db.String(100), db.ForeignKey("como_ubico.forma"))
    como_ubico_otro = db.Column(db.String(256))
    municipio_id = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    sujeto = db.Column(db.String(15))
    edad = db.Column(db.Integer)
    identidad_genero_id = db.Column(db.String(100), db.ForeignKey('identidad_genero.tipo'))
    pronombre = db.Column(db.String(5))
    grupo_conviviente = db.Column(db.String(50))
    grupo_conviviente_otro = db.Column(db.String(50))
    detalle_motivo_id = db.Column(db.String(100), db.ForeignKey("detalle_motivo_consulta.motivo"))
    malestar_emocional_id = db.Column(db.String(100), db.ForeignKey("malestar_emocional.tipo"))
    # TODO: Tengo que seguir con Situaciones de Vulnerabilidad

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