from src.core.database import db

class Dispositivo(db.Model):
    """ Clase que representa el modelo de dispositivos del PBA que pueden realizar derivaciones a CETECSM """
    __tablename__ = "dispositivos"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def update(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)