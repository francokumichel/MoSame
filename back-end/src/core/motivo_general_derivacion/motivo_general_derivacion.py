from src.core.database import db

class MotivoGeneralDerivacion(db.Model):
    """ Clase que representa el modelo de tipos de motivos generales de derivacion """
    __tablename__ = "motivo_general_derivacion"

    tipo = db.Column(db.String(100), primary_key=True)
    otro_tipo = db.Column(db.String(100))
    derivaciones = db.relationship("Derivacion", backref="mot_gral_derivacion")    