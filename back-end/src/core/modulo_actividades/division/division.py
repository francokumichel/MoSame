from src.core.database import db

class Division(db.Model):
    __tablename__ = "division"

    nombre = db.Column(db.String(5), primary_key=True)