from src.core.database import db
from src.core.municipio.municipio import Municipio

def create(**kwargs):
    municipio = Municipio(**kwargs)
    db.session.add(municipio)
    db.session.commit()
    return municipio