from src.core.database import db
from src.core.motivo_general_acompanamiento.motivo_general_acompanamiento import MotivoGeneralAcompanamiento

def create_mot_gral_acomp(**kwargs):
    motivo_gral_acomp = MotivoGeneralAcompanamiento(**kwargs)
    db.session.add(motivo_gral_acomp)
    db.session.commit()
    return motivo_gral_acomp

def list_mot_gral_acomp():
    return MotivoGeneralAcompanamiento.query.all()

def get_motivo_gral_acomp_by_tipo(tipo):
    return MotivoGeneralAcompanamiento.query.filter_by(tipo=tipo).first()

def vaciar_mot_gral_acomp():
    try:
        # Elimina todas las tuplas de la tabla
        db.session.query(MotivoGeneralAcompanamiento).delete()
        db.session.commit()
        return True
    except Exception as e:
        # Maneja cualquier error que ocurra durante la eliminación
        db.session.rollback()
        print("Error al vaciar la tabla:", str(e))
        return False