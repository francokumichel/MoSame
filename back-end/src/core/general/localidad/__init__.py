from src.core.database import db
from src.core.general.localidad.localidad import Localidad

def create_localidad(**kwargs):
    localidad = Localidad(**kwargs)
    db.session.add(localidad)
    db.session.commit()
    return localidad

def list_localidades():
    return Localidad.query.all()

def vaciar_localidades():
    try:
        # Elimina todas las tuplas de la tabla
        db.session.query(Localidad).delete()
        db.session.commit()
        return True
    except Exception as e:
        # Maneja cualquier error que ocurra durante la eliminación
        db.session.rollback()
        print("Error al vaciar la tabla:", str(e))
        return False