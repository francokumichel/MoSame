from src.core.prueba.prueba import Prueba
from src.core.database import db

def create_prueba(**kwargs):
    prueba = Prueba(**kwargs)
    db.session.add(prueba)
    db.session.commit()
    return prueba

def delete_prueba(id):
    prueba = Prueba.query.get(id)
    db.session.delete(prueba)
    db.session.commit()
    return prueba

def list_prueba():
    pruebas = Prueba.query.all()
    print(pruebas)
    return pruebas