from src.core.database import db
from src.core.llamada_cetecsm.llamada_cetecsm import LlamadaCetecsm

def create_llamada_cetecsm(**kwargs):
    llamada_cetecsm = LlamadaCetecsm(**kwargs)
    db.session.add(llamada_cetecsm)
    db.session.commit()
    return llamada_cetecsm