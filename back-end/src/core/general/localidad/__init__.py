from src.core.database import db
from src.core.general.localidad.localidad import Localidad

def create_localidad(**kwargs):
    localidad = Localidad(**kwargs)
    db.session.add(localidad)
    db.session.commit()
    return localidad

def list_municipios():
    return Localidad.query.all()