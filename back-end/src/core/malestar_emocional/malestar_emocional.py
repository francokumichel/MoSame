from src.core.database import db

class MalestarEmocional(db.Model):
    """ Clase que representa el modelo de tipos de malestares emocionales """
    __tablename__ = "malestar_emocional"

    tipo = db.Column(db.String(100), primary_key=True)