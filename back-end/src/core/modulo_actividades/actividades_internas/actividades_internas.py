from src.core.database import db

class ActividadesInternas(db.Model):
    __tablename__ = "actividades_internas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))