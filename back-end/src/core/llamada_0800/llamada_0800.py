from src.core.database import db
import enum
from sqlalchemy import func
from src.core.general.municipio.municipio import Municipio

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
    motivo_nombre = db.Column(db.String(100))
    como_ubico_forma = db.Column(db.String(100))
    como_ubico_otro = db.Column(db.String(256))
    municipio_nombre = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    sujeto = db.Column(db.String(15))
    edad = db.Column(db.Integer)
    identidad_genero_tipo = db.Column(db.String(100))
    identidad_genero_otra = db.Column(db.String(100))
    pronombre = db.Column(db.String(5))
    grupo_conviviente = db.Column(db.String(50))
    grupo_conviviente_otro = db.Column(db.String(50))
    detalle_motivo_motivo = db.Column(db.String(100))
    malestares_emocionales = db.Column(db.Text)
    malestares_emocionales_otro = db.Column(db.String(100))
    situaciones_vulnerabilidad = db.Column(db.Text)
    definicion = db.Column(db.String(100))
    persona_cetecsm_id = db.Column(db.Integer)
    intervencion_sugerida = db.Column(db.String(100))
    motivo_derivacion = db.Column(db.String(100))
    motivo_derivacion_otro = db.Column(db.String(100))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    dni = db.Column(db.String(10))
    telefonos = db.Column(db.Text)
    emails = db.Column(db.Text)
    domicilio = db.Column(db.String(256))
    nacionalidad = db.Column(db.String(50))
    nacimiento = db.Column(db.Date)
    detalle_intervencion = db.Column(db.Text)
    duracion = db.Column(db.String(50))
    demanda_tratamiento = db.Column(db.Boolean())
    email_operador = db.Column(db.String(100))
    fecha_y_hora_carga = db.Column(db.DateTime, default=func.current_timestamp())