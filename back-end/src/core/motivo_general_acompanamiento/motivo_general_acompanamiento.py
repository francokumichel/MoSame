from src.core.database import db

mot_acom_malestar_emoc = db.Table("Mot_acom_malestar_emoc", 
    db.Column("mot_gral_acomp_id", db.String(100), db.ForeignKey("motivo_general_acompanamiento.tipo"), primary_key=True),
    db.Column("malestar_emocional_id", db.String(100), db.ForeignKey("malestar_emocional.tipo"), primary_key=True)                                  
)

class MotivoGeneralAcompanamiento(db.Model):
    """ Clase que representa el modelo de los motivos generales de acompañamiento """
    __tablename__ = "motivo_general_acompanamiento"

    tipo = db.Column(db.String(100), primary_key=True)