from src.core.database import db

class ActividadesInternas(db.Model):
    __tablename__ = "actividades_internas"

    nombre = db.Column(db.String(100), primary_key=True)
    actividadades = db.relationship("Actividad", backref="actividad_interna")