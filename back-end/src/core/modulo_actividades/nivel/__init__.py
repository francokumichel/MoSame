from src.core.database import db
from src.core.modulo_actividades.nivel.nivel import Nivel

def create_nivel(**kwargs):
    nivel = Nivel(**kwargs)
    db.session.add(nivel)
    db.session.commit()
    return nivel

def get_by_name(name):
    return Nivel.query.filter_by(nombre=name).first()