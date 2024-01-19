from src.core.database import db
from src.core.llamada_cetecsm.llamada_cetecsm import LlamadaCetecsm

def create_llamada_cetecsm(**kwargs):
    llamada_cetecsm = LlamadaCetecsm(**kwargs)
    db.session.add(llamada_cetecsm)
    db.session.commit()
    return llamada_cetecsm

def obtener_fecha_ultimo_llamado(persona_id):
    # Supongamos que LlamadaCetecsm es el modelo de llamada y fecha_llamado es el campo de fecha
    ultima_llamada = LlamadaCetecsm.query.filter_by(persona_cetecsm_id=persona_id).order_by(LlamadaCetecsm.fecha_llamado.desc()).first()

    if ultima_llamada:
        return ultima_llamada.fecha_llamado
    else:
        # Devolver una fecha predeterminada o None según tu lógica
        return None