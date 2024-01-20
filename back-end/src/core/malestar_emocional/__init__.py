from src.core.database import db
from src.core.malestar_emocional.malestar_emocional import MalestarEmocional

def create(**kwargs):
    malestar_emocional = MalestarEmocional(**kwargs)
    db.session.add(malestar_emocional)
    db.session.commit()
    return malestar_emocional

def list_malestares_emocionales():
    return MalestarEmocional.query.all()

def get_malestar_emocional_by_tipo(tipo):
    return MalestarEmocional.query.filter_by(tipo=tipo).first()