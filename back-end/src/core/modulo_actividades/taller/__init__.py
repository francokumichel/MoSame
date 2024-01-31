from src.core.database import db
from src.core.modulo_actividades.taller.taller import Taller
from src.core.modulo_actividades.actividad.actividad import Actividad

def create_taller(**kwargs):
    taller = Taller(**kwargs)
    db.session.add(taller)
    db.session.commit()
    return taller

def get_talleres(tipo_actividad, page, per_page):
    
    talleres = Taller.query
    
    if tipo_actividad:
        talleres = talleres.filter(Taller.actividad.has(Actividad.tipo == tipo_actividad))
    
    return talleres.order_by(Taller.id).paginate(page=page, per_page=per_page, error_out=True)