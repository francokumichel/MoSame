from src.core.database import db
from src.core.modulo_actividades.taller.taller import Taller, TiposActividades
from src.core.modulo_actividades.actividad.actividad import Actividad
from sqlalchemy import case

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