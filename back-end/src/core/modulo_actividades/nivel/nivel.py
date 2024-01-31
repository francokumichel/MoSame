from src.core.database import db

class Nivel(db.Model):
    __tablename__ = "nivel"

    nombre = db.Column(db.String(100), primary_key=True)