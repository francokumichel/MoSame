from src.core.database import db
from src.core.persona_cetecsm.persona_cetecsm import PersonaCetecsm

def create(**kwargs):
    persona_cetecsm = PersonaCetecsm(**kwargs)
    db.session.add(persona_cetecsm)
    db.session.commit()
    return persona_cetecsm