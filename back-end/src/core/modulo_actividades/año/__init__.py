from src.core.database import db
from src.core.modulo_actividades.año.anio import Anio

def create_anio(**kwargs):
    anio = Anio(**kwargs)
    db.session.add(anio)
    db.session.commit()
    return anio
