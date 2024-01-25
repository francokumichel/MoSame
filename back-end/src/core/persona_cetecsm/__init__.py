from src.core.database import db
from sqlalchemy import func, desc, and_
from sqlalchemy.orm import aliased
from src.core.persona_cetecsm.persona_cetecsm import PersonaCetecsm, Municipio, RegionSanitaria
from src.core.llamada_cetecsm.llamada_cetecsm import LlamadaCetecsm
from src.core.derivacion.derivacion import Derivacion
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

def list_regiones_sanitarias():
    return RegionSanitaria.query.all()

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

def get_personas_cetecsm_todas(search_terms, page_num, per_page):
    
    query = PersonaCetecsm.query
    if search_terms:
        dict_functions = {
            'regiones_sanitarias': buscar_personas_por_regiones,
            'dispositivo_derivador': buscar_personas_por_dispositivo,
            'fechas': buscar_personas_por_fecha_derivacion,
            'edades': buscar_personas_por_edad,
            'motivo_derivacion': buscar_personas_por_motivo_derivacion,
            'operador': buscar_personas_por_operador
        }
        for key, value in search_terms.items():
            if value:
                query = dict_functions[key](query, value)
                
    return query.order_by(PersonaCetecsm.id).paginate(page=page_num, per_page=per_page, error_out=True)

def get_personas_cetecsm_todas_sin_paginar(search_terms):
    
    query = PersonaCetecsm.query
    if search_terms:
        dict_functions = {
            'regiones_sanitarias': buscar_personas_por_regiones,
            'dispositivo_derivador': buscar_personas_por_dispositivo,
            'fechas': buscar_personas_por_fecha_derivacion,
            'edades': buscar_personas_por_edad,
            'motivo_derivacion': buscar_personas_por_motivo_derivacion,
            'operador': buscar_personas_por_operador
        }
        for key, value in search_terms.items():
            if value:
                query = dict_functions[key](query, value)
                
    return query        

def get_all_personas_asignadas(page_num, per_page):
    """ Consulta a la BD y obtiene los registros páginados de las personas cetecsm que estás asigaadas a algún operador cetecsm"""
    personas_asignadas = PersonaCetecsm.query.filter_by(esta_asignada=True)
    return personas_asignadas.order_by(PersonaCetecsm.id).paginate(page=page_num, per_page=per_page, error_out=True)

def list_all_personas_cetecsm_no_asignadas(page_num, per_page):
    """ Consulta a la bd y obtiene los registros paginados de los usuarios registrados en el sistema """
    resultados = PersonaCetecsm.query.filter_by(esta_asignada=False)

    return resultados.order_by(PersonaCetecsm.id).paginate(page=page_num, per_page=per_page, error_out=True)
    
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

def buscar_personas_por_regiones(query, regiones_sanitarias):
    return query.filter(PersonaCetecsm.municipio.has(Municipio.region_sanitaria_id.in_(regiones_sanitarias)))

def buscar_personas_por_dispositivo(query, dispositivo):
    return query.filter(PersonaCetecsm.derivacion.has(Derivacion.dispositivo_derivacion.ilike(f"%{dispositivo}%")))

def buscar_personas_por_fecha_derivacion(query, fechas):
    if fechas['desde'] and fechas['hasta']:
        return query.filter(PersonaCetecsm.derivacion.has(Derivacion.fecha.between(fechas['desde'], fechas['hasta'])))
    elif fechas['desde']:
        return query.filter(PersonaCetecsm.derivacion.has(Derivacion.fecha >= fechas['desde']))
    elif fechas['hasta']:
        return query.filter(PersonaCetecsm.derivacion.has(Derivacion.fecha <= fechas['hasta']))

    return query

def buscar_personas_por_edad(query, edades):
    if edades['desde'] and edades['hasta']:
        return query.filter(PersonaCetecsm.edad.between(edades['desde'], edades['hasta']))
    elif edades['desde']:
        return query.filter(PersonaCetecsm.edad >= edades['desde'])
    elif edades['hasta']:
        return query.filter(PersonaCetecsm.edad <= edades['hasta'])

    return query
    
def buscar_personas_por_motivo_derivacion(query, motivo_derivacion):
    return query.filter(PersonaCetecsm.derivacion.has(Derivacion.tipo_motivo_gral == motivo_derivacion))

def buscar_personas_por_operador(query, operador):
    return query.filter(PersonaCetecsm.derivacion.has(Derivacion.nombre_operador_derivador == operador))
