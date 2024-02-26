from src.core.database import db
from src.core.modulo_actividades.actividades_externas.actividades_externas import ActividadesExternas

def create_actividad_externa(**kwargs):
    actividad_externa = ActividadesExternas(**kwargs)
    db.session.add(actividad_externa)
    db.session.commit()
    return actividad_externa

def list_actividades_externas():
    return ActividadesExternas.query.all()

def vaciar_acctividades_externas():
    try:
        # Elimina todas las tuplas de la tabla
        db.session.query(ActividadesExternas).delete()
        db.session.commit()
        return True
    except Exception as e:
        # Maneja cualquier error que ocurra durante la eliminación
        db.session.rollback()
        print("Error al vaciar la tabla:", str(e))
        return False