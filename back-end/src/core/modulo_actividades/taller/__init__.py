from src.core.database import db
from src.core.modulo_actividades.taller.taller import Taller, TiposActividades
from src.core.modulo_actividades.actividad.actividad import Actividad

def create_taller(**kwargs):
    taller = Taller(**kwargs)
    db.session.add(taller)
    db.session.commit()
    return taller

def get_talleres(tipo_actividad, page, per_page):
    
    talleres = Taller.query
    
    if tipo_actividad:
        talleres = talleres.filter(Taller.tipo == tipo_actividad)
    
    return talleres.order_by(Taller.id).paginate(page=page, per_page=per_page, error_out=True)

def get_talleres_todos(search_terms, page_num, per_page):
    
    query = Taller.query
    if search_terms:
        dict_functions = {
            'regiones_sanitarias': buscar_talleres_por_regiones,
            'fechas': buscar_talleres_por_fecha,
            'municipio': buscar_talleres_por_municipio,
            'gestion': buscar_talleres_por_gestion
        }
        for key, value in search_terms.items():
            if value:
                query = dict_functions[key](query, value)
                
    return query.order_by(Taller.id).paginate(page=page_num, per_page=per_page, error_out=True)

def get_talleres_todos_sin_paginar(search_terms):
    
    query = Taller.query
    if search_terms:
        dict_functions = {
            'regiones_sanitarias': buscar_talleres_por_regiones,
            'fechas': buscar_talleres_por_fecha,
            'municipio': buscar_talleres_por_municipio,
            'gestion': buscar_talleres_por_gestion
        }
        for key, value in search_terms.items():
            if value:
                query = dict_functions[key](query, value)
                
    return query

def buscar_talleres_por_regiones(query, regiones_sanitarias):
    from src.core.general.municipio.municipio import Municipio
    return query.filter(Taller.municipio.has(Municipio.region_sanitaria_id.in_(regiones_sanitarias)))

def buscar_talleres_por_fecha(query, fechas):
    if fechas['desde'] and fechas['hasta']:
        return query.filter(Taller.fecha_hora_carga.between(fechas['desde'], fechas['hasta']))
    elif fechas['desde']:
        return query.filter(Taller.fecha_hora_carga >= fechas['desde'])
    elif fechas['hasta']:
        return query.filter(Taller.fecha_hora_carga <= fechas['hasta'])

    return query
    
def buscar_talleres_por_municipio(query, municipio):
    return query.filter(Taller.municipio_id == municipio)

def buscar_talleres_por_gestion(query, gestion):
    from src.core.modulo_actividades.escuela.escuela import Escuela
    return query.filter(Taller.actividad.has(Actividad.escuela.has(Escuela.sector == gestion)))

def obtener_estadisticas(tipo_taller, agrupar_por, actividad, page, per_page):

    # Realizo una importación local para evitar el error de importación circular
    from src.core.general.municipio.municipio import Municipio

    campo_a_mostrar = (
        db.func.extract('year', Taller.fecha_hora_carga).label('fecha_hora_carga') if agrupar_por == 'fecha_hora_carga' else
        getattr(Taller, agrupar_por) if agrupar_por != 'region_sanitaria_id' else Municipio.region_sanitaria_id
    )
    
    filtro_actividad = {
        TiposActividades.TALLERES.value: True,
        TiposActividades.ESPACIO_GRUPAL.value: True if actividad == 'Todas' else Actividad.actividad == actividad,
        TiposActividades.ACCIONES_PROMOCION.value: True if actividad == 'Todas' else Actividad.actividad == actividad,
    }

    result = db.session.query( 
        campo_a_mostrar, 
        db.func.count(Taller.id).label('cant_talleres'), 
        db.func.sum(Actividad.cant_encuentros).label('cant_encuentros'), 
        db.func.count(Actividad.escuela_cue.distinct()).label('cant_escuelas'), 
        db.func.sum(Actividad.cant_participantes).label('cant_participantes')
    ).filter(
        Taller.tipo == tipo_taller, filtro_actividad[tipo_taller]
    ).join(
        Actividad, 
        Taller.id == Actividad.taller_id
    ).join(
        Municipio,
        Taller.municipio_id == Municipio.nombre
    ).group_by(campo_a_mostrar)

    return result.order_by(campo_a_mostrar).paginate(page=page, per_page=per_page)