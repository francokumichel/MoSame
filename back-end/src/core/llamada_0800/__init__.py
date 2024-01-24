from src.core.database import db
from src.core.llamada_cetecsm.llamada_cetecsm import LlamadaCetecsm
from src.core.llamada_0800.llamada_0800 import MotivoDeLaConsulta, ComoUbico

def create_llamada_cetecsm(**kwargs):
    llamada_cetecsm = LlamadaCetecsm(**kwargs)
    db.session.add(llamada_cetecsm)
    db.session.commit()
    return llamada_cetecsm

def create_motivo_consulta(**kwargs):
    motivo_consulta = MotivoDeLaConsulta(**kwargs)
    db.session.add(motivo_consulta)
    db.session.commit()
    return motivo_consulta

def list_motivos_consulta():
    return MotivoDeLaConsulta.query.all()

def get_motivo_consulta(nombre):
    return MotivoDeLaConsulta.query.filter_by(nombre=nombre).first()

def create_como_ubico(**kwargs):
    como_ubico = ComoUbico(**kwargs)
    db.session.add(como_ubico)
    db.session.commit()
    return como_ubico

def list_como_ubico():
    return ComoUbico.query.all()

def get_como_ubico(forma):
    return ComoUbico.query.filter_by(forma=forma).first()