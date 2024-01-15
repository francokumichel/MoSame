from src.core.database import db
from src.core.derivacion.derivacion import Derivacion
from src.core.motivo_general_derivacion import get_mot_gral_derivacion_by_tipo
from src.core.malestar_emocional import get_malestar_emocional_by_tipo

def create_derivation(**kwargs):
    nueva_derivacion = Derivacion(**kwargs)
    db.session.add(nueva_derivacion)
    db.session.commit()
    return nueva_derivacion

def actualizar_derivacion(derivacion, mot_gral_derivacion):
    mot_gral_derivacion_nuevo = get_mot_gral_derivacion_by_tipo(tipo=mot_gral_derivacion['tipo'])
    if mot_gral_derivacion['tipo'] == "Otro": 
        mot_gral_derivacion_nuevo.otro_tipo = mot_gral_derivacion['otro_tipo']

    derivacion.mot_gral_derivacion = mot_gral_derivacion_nuevo
    db.session.commit()
    return derivacion
    