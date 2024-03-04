from src.core.database import db
from src.core.situaciones_vulnerabilidad import situacion_vulnerabilidad
import enum

class GrupoConviviente(enum.Enum):
    """ Tipo enumerativo que define los grupos convivientes """
    S = "Solo"
    AM = "Con adultos/as y menores"
    A = "Solo con adulto/as"
    M = "Solo con menores"
    O = "Otro"

personacetecsm_sit_vuln = db.Table('personacetecsm_sit_vul',   
    db.Column('persona_cetecsm_id', db.Integer, db.ForeignKey('persona_cetecsm.id'), primary_key=True),
    db.Column('sit_vuln_id', db.String(100), db.ForeignKey('situaciones_vulnerabilidad.tipo'), primary_key=True)                                
)

#class RegionSanitaria(db.Model):
#    __tablename__ = "region_sanitaria"
#
#    tipo = db.Column(db.String(50), primary_key=True)
#    personas_cetecsm = db.relationship("Municipio", backref="region_sanitaria")

#class Municipio(db.Model):
#    __tablename__ = "municipio"
#
#    nombre = db.Column(db.String(100), primary_key=True)
#    region_sanitaria_id = db.Column(db.String(50), db.ForeignKey('region_sanitaria.tipo'))
#    personas_cetecsm = db.relationship("PersonaCetecsm", backref="municipio")

class PersonaCetecsm(db.Model):
    """ Clase que representa el modelo de una persona derivada a CETECSM """
    __tablename__ = "persona_cetecsm"

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(25))
    grupo_conviviente = db.Column(db.String(50))
    grupo_conviviente_otro = db.Column(db.String(50))
    dio_consentimiento = db.Column(db.Boolean())
    localidad = db.Column(db.String(255))
    tiene_obra_social = db.Column(db.Boolean())
    esta_asignada = db.Column(db.Boolean(), default=False)
    obra_social = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    telefono = db.Column(db.String(255))
    telefono_alternativo = db.Column(db.String(255))
    detalle_acompanamiento = db.Column(db.Text, default='')
    fecha_prox_llamado_actual = db.Column(db.Date) 
    derivacion = db.relationship('Derivacion', backref="persona_cetecsm_derivada", uselist=False)
    llamadas_cetecsm = db.relationship("LlamadaCetecsm", backref="persona_cetecsm_llamada")
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    identidad_genero_id = db.Column(db.String(100))
    identidad_genero_otra = db.Column(db.String(100))
    motivo_gral_acomp_id = db.Column(db.String(100))
    malestares_emocionales = db.Column(db.Text)
    municipio_id = db.Column(db.String(100), db.ForeignKey('municipio.nombre'))
    situaciones_vulnerabilidad = db.Column(db.Text)
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()