from src.core.database import db
from src.core.llamada_0800.llamada_0800 import Llamada0800
from src.core.llamada_0800.llamada_0800 import MotivoDeLaConsulta, ComoUbico, DetalleMotivoConsulta
from src.core.persona_cetecsm.persona_cetecsm import Municipio

def create_llamada_0800(**kwargs):
    llamada_0800 = Llamada0800(**kwargs)
    db.session.add(llamada_0800)
    db.session.commit()
    return llamada_0800

def create_motivo_consulta(**kwargs):
    motivo_consulta = MotivoDeLaConsulta(**kwargs)
    db.session.add(motivo_consulta)
    db.session.commit()
    return motivo_consulta

def list_motivos_consulta():
    return MotivoDeLaConsulta.query.all()

def get_motivo_consulta(nombre):
    return MotivoDeLaConsulta.query.filter_by(nombre=nombre).first()

def create_como_ubico(**kwargs):
    como_ubico = ComoUbico(**kwargs)
    db.session.add(como_ubico)
    db.session.commit()
    return como_ubico

def list_como_ubico():
    return ComoUbico.query.all()

def get_como_ubico(forma):
    return ComoUbico.query.filter_by(forma=forma).first()

def create_detalle_motivo_consulta(**kwargs):
    detalle_motivo_consulta = DetalleMotivoConsulta(**kwargs)
    db.session.add(detalle_motivo_consulta)
    db.session.commit()
    return detalle_motivo_consulta

def list_detalles_motivo_consulta():
    return DetalleMotivoConsulta.query.all()

def get_detalle_motivo_consulta(motivo):
    return DetalleMotivoConsulta.query.filter_by(motivo=motivo).first()

def list_llamadas_0800(search_term, page_num, per_page):
    """ Consulta a la bd y obtiene los egistros paginados de las llamadas del 0800 """
    if search_term:
        resultados = Llamada0800.query.filter(
            (Llamada0800.telefonos.ilike(f"%{search_term}%")) |
            (Llamada0800.nombre.ilike(f"%{search_term}%")) |
            (Llamada0800.apellido.ilike(f"%{search_term}%")) |
            (Llamada0800.dni.ilike(f"%{search_term}%")) |
            (Llamada0800.municipio_nombre.ilike(f"%{search_term}%"))
        )

        return resultados.order_by(Llamada0800.id).paginate(page=page_num, per_page=per_page, error_out=True)
    return Llamada0800.query.order_by(Llamada0800.id).paginate(page=page_num, per_page=per_page, error_out=True)

def get_llamada_0800_by_id(llamada_id) -> Llamada0800:
    return Llamada0800.query.get(llamada_id)

def get_llamadas_0800_todas(search_terms, page_num, per_page):
    
    query = Llamada0800.query
    if search_terms:
        dict_functions = {
            'regiones_sanitarias': buscar_llamadas_por_regiones,
            'fechas': buscar_llamadas_por_fecha,
            'edades': buscar_llamadas_por_edad,
            'motivo_consulta': buscar_llamadas_por_motivo_consulta,
            'detalle_motivo_consulta': buscar_llamadas_por_detalle_motivo_consulta,
            'genero': buscar_llamadas_por_genero
        }
        for key, value in search_terms.items():
            if value:
                query = dict_functions[key](query, value)
                
    return query.order_by(Llamada0800.id).paginate(page=page_num, per_page=per_page, error_out=True)

def buscar_llamadas_por_regiones(query, regiones_sanitarias):
    return query.filter(Llamada0800.municipio.has(Municipio.region_sanitaria_id.in_(regiones_sanitarias)))

def buscar_llamadas_por_fecha(query, fechas):
    if fechas['desde'] and fechas['hasta']:
        return query.filter(Llamada0800.fecha_y_hora_carga.between(fechas['desde'], fechas['hasta']))
    elif fechas['desde']:
        return query.filter(Llamada0800.fecha_y_hora_carga >= fechas['desde'])
    elif fechas['hasta']:
        return query.filter(Llamada0800.fecha_y_hora_carga <= fechas['hasta'])

    return query

def buscar_llamadas_por_edad(query, edades):
    if edades['desde'] and edades['hasta']:
        return query.filter(Llamada0800.edad.between(edades['desde'], edades['hasta']))
    elif edades['desde']:
        return query.filter(Llamada0800.edad >= edades['desde'])
    elif edades['hasta']:
        return query.filter(Llamada0800.edad <= edades['hasta'])

    return query
    
def buscar_llamadas_por_motivo_consulta(query, motivo_consulta):
    return query.filter(Llamada0800.motivo_nombre == motivo_consulta)
    
def buscar_llamadas_por_detalle_motivo_consulta(query, detalle_motivo_consulta):
    return query.filter(Llamada0800.detalle_motivo_motivo == detalle_motivo_consulta)
    
def buscar_llamadas_por_genero(query, genero):
    return query.filter(Llamada0800.identidad_genero_tipo == genero)