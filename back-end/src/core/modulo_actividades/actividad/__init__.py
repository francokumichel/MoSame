from src.core.database import db
from src.core.modulo_actividades.actividad.actividad import Actividad

def create_actividad(**kwargs):
    actividad = Actividad(**kwargs)
    db.session.add(actividad)
    db.session.commit()
    return actividad

def list_actividades():
    return Actividad.query.all()

def get_by_id(id):
    return Actividad.query.filter_by(id=id).first()