from src.core.database import db
from src.core.modulo_actividades.actividades_internas.actividades_internas import ActividadesInternas

def create_actividad_interna(**kwargs):
    actividad_interna = ActividadesInternas(**kwargs)
    db.session.add(actividad_interna)
    db.session.commit()
    return actividad_interna

def list_actividades_internas():
    return ActividadesInternas.query.all()

def vaciar_acctividades_internas():
    try:
        # Elimina todas las tuplas de la tabla
        db.session.query(ActividadesInternas).delete()
        db.session.commit()
        return True
    except Exception as e:
        # Maneja cualquier error que ocurra durante la eliminación
        db.session.rollback()
        print("Error al vaciar la tabla:", str(e))
        return False