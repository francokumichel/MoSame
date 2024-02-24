from src.core.database import db

class ActividadesExternas(db.Model):
    __tablename__ = "actividades_externas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))