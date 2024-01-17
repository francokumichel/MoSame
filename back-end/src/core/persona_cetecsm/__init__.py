from src.core.database import db
from src.core.persona_cetecsm.persona_cetecsm import PersonaCetecsm, Municipio, RegionSanitaria
from src.core.llamada_cetecsm.llamada_cetecsm import LlamadaCetecsm
from src.core.motivo_general_acompanamiento import get_motivo_gral_acomp_by_tipo
from src.core.malestar_emocional import get_malestar_emocional_by_tipo
from src.core.identidad_genero import get_identidad_genero_by_tipo
from src.core.situaciones_vulnerabilidad import get_situacion_vulnerabilidad_by_tipo

def create_municipio(**kwargs):
    municipio = Municipio(**kwargs)
    db.session.add(municipio)
    db.session.commit()
    return municipio

def list_municipios():
    return Municipio.query.all()

def create_region_sanitaria(**kwargs):
    region_sanitaria = RegionSanitaria(**kwargs)
    db.session.add(region_sanitaria)
    db.session.commit()
    return region_sanitaria

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

def actualizar_mot_gral_acomp(persona, mot_gral_acomp): 

    if mot_gral_acomp:

        if persona.motivo_gral_acomp:
            persona.motivo_gral_acomp.malestares_emocionales = []

        motivo = get_motivo_gral_acomp_by_tipo(tipo=mot_gral_acomp['tipo'])

        if mot_gral_acomp['tipo'] == "Malestar emocional":
            for malestar in mot_gral_acomp['malestares_emocionales']:
                malestar = get_malestar_emocional_by_tipo(tipo=malestar['tipo'])
                motivo.malestares_emocionales.append(malestar)

        persona.motivo_gral_acomp = motivo
        db.session.commit()
    return persona

def actualizar_identidad_genero(persona, identidad_genero):
    if identidad_genero:
        identidad_genero_nueva = get_identidad_genero_by_tipo(tipo=identidad_genero['tipo'])
        if identidad_genero['tipo'] == "Otra identidad":
            identidad_genero_nueva['otro_tipo'] = identidad_genero['otro_tipo']
        persona.identidad_genero = identidad_genero_nueva
        db.session.commit()
    return persona

def actualizar_sit_vuln(persona, situaciones_vulnerabilidad):

    if situaciones_vulnerabilidad:
        persona.situaciones_vulnerabilidad = []

        for situacion in situaciones_vulnerabilidad:
            situacion_vulnerabilidad = get_situacion_vulnerabilidad_by_tipo(tipo=situacion['tipo'])
            persona.situaciones_vulnerabilidad.append(situacion_vulnerabilidad)

        db.session.commit()
    return persona 
     