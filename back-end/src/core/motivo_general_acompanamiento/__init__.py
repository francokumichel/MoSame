from src.core.database import db
from src.core.motivo_general_acompanamiento.motivo_general_acompanamiento import MotivoGeneralAcompanamiento

def create(**kwargs):
    motivo_gral_acomp = MotivoGeneralAcompanamiento(**kwargs)
    db.session.add(motivo_gral_acomp)
    db.session.commit()
    return motivo_gral_acomp