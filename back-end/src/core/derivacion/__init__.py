from src.core.database import db
from src.core.derivacion.derivacion import Derivacion

def create_derivation(**kwargs):
    nueva_derivacion = Derivacion(**kwargs)
    db.session.add(nueva_derivacion)
    db.session.commit()
    return nueva_derivacion