from src.core.database import db
from src.core.identidad_genero.identidad_genero import IdentidadGenero

def create_identidad_genero(**kwargs):
    identidad_genero = IdentidadGenero(**kwargs)
    db.session.add(identidad_genero)
    db.session.commit()
    return identidad_genero

def list_identidades_genero():
    return IdentidadGenero.query.all()

def get_identidad_genero_by_tipo(tipo):
    return IdentidadGenero.query.filter_by(tipo=tipo).first()

def vaciar_identidad_genero():
    try:
        # Elimina todas las tuplas de la tabla
        db.session.query(IdentidadGenero).delete()
        db.session.commit()
        return True
    except Exception as e:
        # Maneja cualquier error que ocurra durante la eliminación
        db.session.rollback()
        print("Error al vaciar la tabla:", str(e))
        return False
