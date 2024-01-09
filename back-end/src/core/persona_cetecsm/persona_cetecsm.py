from src.core.database import db
import enum

class GrupoConviviente(enum.Enum):
    """ Tipo enumerativo que define los grupos convivientes """
    S = "Solo"
    AM = "Con adultos/as y menores"
    A = "Solo con adulto/as"
    M = "Solo con menores"

class PersonaCetecsm(db.Model):
    """ Clase que representa el modelo de una persona derivada a CETECSM """
    __tablename__ = "persona_cetecsm"

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(25))
    grupo_conviviente = db.Column(db.String(50))
    dio_consentimiento = db.Column(db.Boolean(), default=False, nullable=False)
    localidad = db.Column(db.String(255))
    tiene_obra_social = db.Column(db.Boolean(), default=False)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    telefono = db.Column(db.String(255))
    telefono_alternativo = db.Column(db.String(255), default='-')
    fecha_prox_llamado_actual = db.Column(db.Date) 
    derivacion = db.relationship('Derivacion', backref="persona_cetecsm_derivada", uselist=False)
    llamadas_cetecsm = db.relationship("LlamadaCetecsm", backref="persona_cetecsm_llamada")
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    identidad_genero_id = db.Column(db.String(100), db.ForeignKey('identidad_genero.tipo'))
#    municipio_nombre = db.Column(db.String(100), db.ForeignKey('municipio.nombre'), nullable=False)
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)