from src.core.database import db
from src.core.motivo_general_derivacion.motivo_general_derivacion import MotivoGeneralDerivacion

def create_motivo_gral_der(**kwargs):
    motivo_gral_der = MotivoGeneralDerivacion(**kwargs)
    db.session.add(motivo_gral_der)
    db.session.commit()
    return motivo_gral_der

def list_mot_gral_derivacion():
    return MotivoGeneralDerivacion.query.all()

def get_mot_gral_derivacion_by_tipo(tipo):
    return MotivoGeneralDerivacion.query.filter_by(tipo=tipo).first()