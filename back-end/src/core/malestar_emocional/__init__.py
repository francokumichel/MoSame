from src.core.database import db
from src.core.malestar_emocional.malestar_emocional import MalestarEmocional

def create_malestar_emocional(**kwargs):
    malestar_emocional = MalestarEmocional(**kwargs)
    db.session.add(malestar_emocional)
    db.session.commit()
    return malestar_emocional

def list_malestares_emocionales():
    return MalestarEmocional.query.all()

def get_malestar_emocional_by_tipo(tipo):
    return MalestarEmocional.query.filter_by(tipo=tipo).first()

def vaciar_malestares_emocionales():
    try:
        # Elimina todas las tuplas de la tabla
        db.session.query(MalestarEmocional).delete()
        db.session.commit()
        return True
    except Exception as e:
        # Maneja cualquier error que ocurra durante la eliminación
        db.session.rollback()
        print("Error al vaciar la tabla:", str(e))
        return False