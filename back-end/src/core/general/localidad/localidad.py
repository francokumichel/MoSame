from src.core.database import db

class Localidad(db.Model):
    __tablename__ = "localidad"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))