from src.core.database import db

class Prueba(db.Model):

    __tablename__ = "prueba"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=False)


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)