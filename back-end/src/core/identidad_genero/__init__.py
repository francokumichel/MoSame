from src.core.database import db
from src.core.identidad_genero.identidad_genero import IdentidadGenero

def create(**kwargs):
    identidad_genero = IdentidadGenero(**kwargs)
    db.session.add(identidad_genero)
    db.session.commit()
    return identidad_genero

def list_identidades_genero():
    return IdentidadGenero.query.all()

def get_identidad_genero_by_tipo(tipo):
    return IdentidadGenero.query.filter_by(tipo=tipo).first()
