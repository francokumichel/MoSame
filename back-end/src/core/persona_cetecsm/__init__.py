from src.core.database import db
from src.core.persona_cetecsm.persona_cetecsm import PersonaCetecsm
from src.core.llamada_cetecsm.llamada_cetecsm import LlamadaCetecsm
from sqlalchemy import or_

def create_persona_cetecsm(**kwargs):
    persona_cetecsm = PersonaCetecsm(**kwargs)
    db.session.add(persona_cetecsm)
    db.session.commit()
    return persona_cetecsm

def get_persona_cetecsm(id):
    persona = PersonaCetecsm.query.get(id)
    return persona

def update_persona_cetecsm(**kwargs):
    persona = get_persona_cetecsm(kwargs["id"])
    persona.update(**kwargs)
    db.session.commit()
    return persona

def list_personas_cetecsm(search_term, page_num, per_page):
    """ Consulta a la bd y obtiene los egistros paginados de los usuarios registrados en el sistema """
    if search_term:
        resultados = PersonaCetecsm.query.filter(
            (PersonaCetecsm.dni.ilike(f"%{search_term}%")) |
            (PersonaCetecsm.nombre.ilike(f"%{search_term}%")) |
            (PersonaCetecsm.apellido.ilike(f"%{search_term}%")) |
            (PersonaCetecsm.localidad.ilike(f"%{search_term}%"))
        )

        return resultados.order_by(PersonaCetecsm.id).paginate(page=page_num, per_page=per_page, error_out=True)
    return PersonaCetecsm.query.order_by(PersonaCetecsm.id).paginate(page=page_num, per_page=per_page, error_out=True)

def list_llamadas_recibidas(page_num, per_page, persona_id):
    llamadas_recibidas = LlamadaCetecsm.query.join(PersonaCetecsm, PersonaCetecsm.id == LlamadaCetecsm.persona_cetecsm_id).filter(PersonaCetecsm.id == persona_id)
    return llamadas_recibidas.order_by(LlamadaCetecsm.id).paginate(page=page_num, per_page=per_page, error_out=True)