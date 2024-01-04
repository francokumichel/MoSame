from src.core.database import db

motivo_malestar_rel = db.Table(
    "motivo_malestar_rel",
    db.Column("motivo_general_tipo", db.String(100), db.ForeignKey("motivo_general_derivacion.tipo"), primary_key=True),
    db.Column("malestar_tipo", db.String(100), db.ForeignKey("malestar_emocional.tipo"), primary_key=True)
)

class MotivoGeneralDerivacion(db.Model):
    """ Clase que representa el modelo de tipos de motivos generales de derivacion """
    __tablename__ = "motivo_general_derivacion"

    tipo = db.Column(db.String(100), primary_key=True)
    derivaciones = db.relationship("Derivacion", backref="mot_gral_derivacion")
    malestares_emocionales = db.relationship("MalestarEmocional", secondary=motivo_malestar_rel, backref="motivos_generales")
    