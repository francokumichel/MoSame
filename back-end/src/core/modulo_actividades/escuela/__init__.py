from src.core.database import db
from src.core.modulo_actividades.escuela.escuela import Escuela

def create_escuela(**kwargs):
    escuela = Escuela(**kwargs)
    db.session.add(escuela)
    db.session.commit()
    return escuela

def get_escuelas_by_municipio(municipio):
    return Escuela.query.filter_by(municipio_id=municipio)