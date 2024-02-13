from src.core.database import db
from src.core.general.municipio.municipio import Municipio

def create_municipio(**kwargs):
    municipio = Municipio(**kwargs)
    db.session.add(municipio)
    db.session.commit()
    return municipio

def list_municipios():
    return Municipio.query.all()

def get_by_name(name):
    return Municipio.query.filter_by(nombre=name).first()

def get_localidades_by_municipio(municipio):
    municipio = get_by_name(name=municipio)
    return municipio.localidades