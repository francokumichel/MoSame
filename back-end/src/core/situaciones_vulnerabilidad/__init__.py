from src.core.database import db
from src.core.situaciones_vulnerabilidad.situacion_vulnerabilidad import SituacionVulnerabilidad

def create_situacion_vulnerabilidad(**kwargs):
    situacion_vulnerabilidad = SituacionVulnerabilidad(**kwargs)
    db.session.add(situacion_vulnerabilidad)
    db.session.commit()
    return situacion_vulnerabilidad

def list_situaciones_vulnerabilidad():
    return SituacionVulnerabilidad.query.all()

def get_situacion_vulnerabilidad_by_tipo(tipo):
    return SituacionVulnerabilidad.query.filter_by(tipo=tipo).first()

def vaciar_situaciones_vulnerabilidad():
    try:
        # Elimina todas las tuplas de la tabla
        db.session.query(SituacionVulnerabilidad).delete()
        db.session.commit()
        return True
    except Exception as e:
        # Maneja cualquier error que ocurra durante la eliminación
        db.session.rollback()
        print("Error al vaciar la tabla:", str(e))
        return False