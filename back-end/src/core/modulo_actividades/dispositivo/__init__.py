from src.core.database import db
from src.core.modulo_actividades.dispositivo.dispositivo import Dispositivo

def create_dispositivo(**kwargs):
    dispositivo = Dispositivo(**kwargs)
    db.session.add(dispositivo)
    db.session.commit()
    return dispositivo

def list_dispositivos():
    return Dispositivo.query.all()