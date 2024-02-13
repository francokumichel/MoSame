from src.core.database import db
from src.core.modulo_actividades.actividades_internas.actividades_internas import ActividadesInternas

def create_actividad_interna(**kwargs):
    actividad_interna = ActividadesInternas(**kwargs)
    db.session.add(actividad_interna)
    db.session.commit()
    return actividad_interna

def list_actividades_internas():
    return ActividadesInternas.query.all()