from src.core.database import db
from src.core.situaciones_vulnerabilidad.situacion_vulnerabilidad import SituacionVulnerabilidad

def create(**kwargs):
    situacion_vulnerabilidad = SituacionVulnerabilidad(**kwargs)
    db.session.add(situacion_vulnerabilidad)
    db.session.commit()
    return situacion_vulnerabilidad