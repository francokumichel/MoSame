from src.core.database import db
from src.core.motivo_general_acompanamiento.motivo_general_acompanamiento import MotivoGeneralAcompanamiento

def create(**kwargs):
    motivo_gral_acomp = MotivoGeneralAcompanamiento(**kwargs)
    db.session.add(motivo_gral_acomp)
    db.session.commit()
    return motivo_gral_acomp

def list_mot_gral_acomp():
    return MotivoGeneralAcompanamiento.query.all()

def get_motivo_gral_acomp_by_tipo(tipo):
    return MotivoGeneralAcompanamiento.query.filter_by(tipo=tipo).first()