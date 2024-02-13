from src.core.database import db
from src.core.modulo_actividades.actividades_externas.actividades_externas import ActividadesExternas

def create_actividad_externa(**kwargs):
    actividad_externa = ActividadesExternas(**kwargs)
    db.session.add(actividad_externa)
    db.session.commit()
    return actividad_externa

def list_actividades_externas():
    return ActividadesExternas.query.all()