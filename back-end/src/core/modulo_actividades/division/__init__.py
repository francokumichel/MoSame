from src.core.database import db
from src.core.modulo_actividades.division.division import Division

def create_division(**kwargs):
    division = Division(**kwargs)
    db.session.add(division)
    db.session.commit()
    return division