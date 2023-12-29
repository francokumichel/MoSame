from src.core.database import db

class Derivacion(db.Model):
    """ Clase que representa el modelo de una derivación realizada por un efector del PBA a CETECSM """
    __tablename__ = "derivaciones"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    dispositivo_derivacion = db.Column(db.String(70))
    nombre_operador_derivador = db.Column(db.String(70))
    descripcion = db.Column(db.String(255))
    tipo_motivo_gral = db.Column(db.String(100), db.ForeignKey('motivo_general_derivacion.tipo'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    persona_cetecsm_id = db.Column(db.Integer, db.ForeignKey('persona_cetecsm.id'), unique=True, nullable=False)