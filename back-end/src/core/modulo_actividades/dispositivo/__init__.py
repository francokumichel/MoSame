from src.core.database import db
from src.core.modulo_actividades.dispositivo.dispositivo import Dispositivo

def create_dispositivo(**kwargs):
    dispositivo = Dispositivo(**kwargs)
    db.session.add(dispositivo)
    db.session.commit()
    return dispositivo

def list_dispositivos():
    return Dispositivo.query.all()

def vaciar_dispositivos():
    try:
        # Elimina todas las tuplas de la tabla
        db.session.query(Dispositivo).delete()
        db.session.commit()
        return True
    except Exception as e:
        # Maneja cualquier error que ocurra durante la eliminación
        db.session.rollback()
        print("Error al vaciar la tabla:", str(e))
        return False