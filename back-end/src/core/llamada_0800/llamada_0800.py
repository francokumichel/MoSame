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
    
llamada0800_sit_vuln = db.Table('llamada0800_sit_vul',   
    db.Column('llamada_id', db.Integer, db.ForeignKey('llamada_0800.id'), primary_key=True),
    db.Column('sit_vuln_id', db.String(100), db.ForeignKey('situaciones_vulnerabilidad.tipo'), primary_key=True)
)

class DefinicionLlamada(enum.Enum):
    FINALIZADA = "Intervención finalizada"
    DERIVADA = "Derivación a CETEC SM"

class IntervecionSugerida(enum.Enum):
    TRATAMIENTO = "Solicita tratamiento ambulatorio"
    NECESIDAD = "Despejar necesidad de medicación / Indicadores de riesgo / Evaluación psiquiátrica"
    APOYO = "Construcción de redes y sistema de apoyo"
    ACOMPANAMIENTO = "Acompañamiento"

class Telefono(db.Model):
    __tablename__ = "telefono"

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(25))
    es_fijo = db.Column(db.Boolean)
    es_propio = db.Column(db.Boolean)
    llamada0800_id = db.Column(db.Integer, db.ForeignKey("llamada_0800.id"))

class Email(db.Model):
    __tablename__ = "email"

    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(100))
    es_propio = db.Column(db.Boolean)
    llamada0800_id = db.Column(db.Integer, db.ForeignKey("llamada_0800.id"))

class Llamada0800(db.Model):
    __tablename__ = "llamada_0800"

    id = db.Column(db.Integer, primary_key=True)
    motivo_id = db.Column(db.String(100), db.ForeignKey("motivo_consulta.nombre"), nullable=False)
    como_ubico_id = db.Column(db.String(100), db.ForeignKey("como_ubico.forma"))
    como_ubico_otro = db.Column(db.String(256))
    municipio_id = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    sujeto = db.Column(db.String(15), nullable=False)
    edad = db.Column(db.Integer)
    identidad_genero_id = db.Column(db.String(100), db.ForeignKey('identidad_genero.tipo'))
    pronombre = db.Column(db.String(5))
    grupo_conviviente = db.Column(db.String(50))
    grupo_conviviente_otro = db.Column(db.String(50))
    detalle_motivo_id = db.Column(db.String(100), db.ForeignKey("detalle_motivo_consulta.motivo"), nullable=False)
    malestar_emocional_id = db.Column(db.String(100), db.ForeignKey("malestar_emocional.tipo"))
    situaciones_vulnerabilidad = db.relationship('SituacionVulnerabilidad', secondary=llamada0800_sit_vuln, backref="llamada0800")
    definicion = db.Column(db.String(100), nullable=False)
    intervencion_sugerida = db.Column(db.String(100))
    tipo_motivo_gral = db.Column(db.String(100), db.ForeignKey('motivo_general_derivacion.tipo'))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    dni = db.Column(db.String(10))
    telefonos = db.relationship("Telefono")
    emails = db.relationship("Email")
    domicilio = db.Column(db.String(256))
    nacionalidad = db.Column(db.String(50))
    nacimiento = db.Column(db.Date)
    detalle_intervencion = db.Column(db.Text, nullable=False)
    fecha_intervencion = db.Column(db.Date, nullable=False)
    duracion = db.Column(db.String(50), nullable=False)
    demanda_tratamiento = db.Column(db.Boolean, nullable=False)
    email_operador = db.Column(db.String(100), nullable=False)
    fecha_y_hora_carga = db.Column(db.DateTime, default=func.current_timestamp())