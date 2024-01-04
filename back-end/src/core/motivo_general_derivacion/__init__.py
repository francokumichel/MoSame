from src.core.database import db
from src.core.motivo_general_derivacion.motivo_general_derivacion import MotivoGeneralDerivacion

def create_motivo_gral_der(**kwargs):
    motivo_gral_der = MotivoGeneralDerivacion(**kwargs)
    db.session.add(motivo_gral_der)
    db.session.commit()
    return motivo_gral_der