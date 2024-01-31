from src.core.database import db

class ActividadesExternas(db.Model):
    __tablename__ = "actividades_externas"

    nombre = db.Column(db.String(100), primary_key=True)
    actividadades = db.relationship("Actividad", backref="actividad_externa")