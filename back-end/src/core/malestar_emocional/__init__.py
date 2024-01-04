from src.core.database import db
from src.core.malestar_emocional.malestar_emocional import MalestarEmocional

def create(**kwargs):
    malestar_emocional = MalestarEmocional(**kwargs)
    db.session.add(malestar_emocional)
    db.session.commit()
    return malestar_emocional