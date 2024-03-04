import json, os
from io import StringIO
from flask import (
    Blueprint,
    jsonify,
    make_response,
    request,
    send_file
)

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)

from src.web.utils.converter import convert_to_csv
from src.core.permissions import list_roles
from src.core.users import find_user_by_email, get_user, create_user, get_roles, update_roles, list_users, asignar_persona, get_personas_asignadas, get_operadores_cetecsm, obtener_total_llamados_cetecsm, obtener_usuario_por_rol
from src.core.schemas.user import user_schema, users_schema
from src.core.persona_cetecsm import create_persona_cetecsm, list_all_personas_cetecsm_no_asignadas, get_persona_cetecsm, list_llamadas_recibidas, generar_sintesis_detalles, get_all_personas_asignadas, get_personas_cetecsm_todas, get_personas_cetecsm_todas_sin_paginar, obtener_informacion_personas_seguimiento, obtener_datos_resolucion_fecha_llamada
from src.core.schemas.persona_cetecsm import persona_cetecsm_schemas, personas_cetecsm_schemas, personas_cetecsm_exportar_schemas
from src.core.general.municipio import get_by_name, list_municipios, get_localidades_by_municipio
from src.core.schemas.municipio import municipios_schema
from src.core.general.region_sanitaria import list_regiones_sanitarias
from src.core.schemas.region_sanitaria import regiones_sanitarias_schema
from src.core.schemas.role import roles_schema
from src.core.derivacion import actualizar_derivacion
from src.core.motivo_general_derivacion import list_mot_gral_derivacion
from src.core.schemas.motivo_general_derivacion import mot_grales_deriv_schema
from src.core.derivacion import create_derivation
from src.core.llamada_cetecsm import create_llamada_cetecsm, obtener_fecha_ultimo_llamado, obtener_cantidad_llamadas, obtener_resolucion_ultima_llamada
from src.core.llamada_cetecsm.llamada_cetecsm import ResolucionLlamado
from src.core.schemas.llamada_cetecsm import llamadas_cetecsm_schema
from src.core import prueba
from src.core.schemas.prueba import prueba_schema
from src.core.motivo_general_acompanamiento import create_mot_gral_acomp, list_mot_gral_acomp, vaciar_mot_gral_acomp
from src.core.schemas.motivo_general_acompanamiento import mot_grales_acomp_schema
from src.core.persona_cetecsm.persona_cetecsm import GrupoConviviente
from src.core.identidad_genero import create_identidad_genero, list_identidades_genero, vaciar_identidad_genero
from src.core.schemas.identidad_genero import identidades_genero_schema
from src.core.malestar_emocional import create_malestar_emocional, list_malestares_emocionales, vaciar_malestares_emocionales
from src.core.schemas.malestar_emocional import malestares_emocionales_schema
from src.core.situaciones_vulnerabilidad import create_situacion_vulnerabilidad, list_situaciones_vulnerabilidad, vaciar_situaciones_vulnerabilidad
from src.core.schemas.situacion_vulnerabilidad import situaciones_vuln_schema
from src.core.modulo_actividades.taller import get_talleres, get_talleres_escuelas_todos, get_talleres_escuelas_todos_sin_paginar, obtener_estadisticas
from src.core.modulo_actividades.taller.taller import TiposActividades
from src.core.schemas.taller import talleres_schema, talleres_schema_observatorio
from src.core.modulo_actividades.dispositivo import create_dispositivo, list_dispositivos, vaciar_dispositivos
from src.core.schemas.dispositivo import dispositivos_schema
from src.core.modulo_actividades.actividades_internas import create_actividad_interna, list_actividades_internas, vaciar_acctividades_internas
from src.core.schemas.actividades_internas import actividades_internas_schema
from src.core.modulo_actividades.actividades_externas import create_actividad_externa, list_actividades_externas, vaciar_acctividades_externas
from src.core.schemas.actividades_externas import actividades_externas_schema
from src.core.modulo_actividades.año.anio import Anios, Divisiones
from src.core.modulo_actividades.año import create_anio
from src.core.modulo_actividades.escuela import get_escuelas_by_municipio
from src.core.modulo_actividades.escuela.escuela import Sectores
from src.core.general.localidad import create_localidad, list_localidades, vaciar_localidades
from src.core.schemas.escuela import escuela_schema, escuelas_schema
from src.core.schemas.localidad import localidades_schema
from src.core.modulo_actividades.actividad import create_actividad
from src.core.modulo_actividades.taller import create_taller
from src.core.llamada_0800 import get_llamadas_0800_todas, get_llamadas_0800_todas_sin_paginar, list_como_ubico, list_detalles_motivo_consulta, list_llamadas_0800, list_motivos_consulta, create_llamada_0800, get_llamada_0800_by_id
from src.core.llamada_0800 import create_como_ubico, create_detalle_motivo_consulta, create_motivo_consulta, get_llamadas_0800_todas, get_llamadas_0800_todas_sin_paginar, list_como_ubico, list_detalles_motivo_consulta, list_llamadas_0800, list_motivos_consulta, create_llamada_0800, get_llamada_0800_by_id, vaciar_como_ubico, vaciar_detalles_motivo_consulta, vaciar_motivos_consulta
from src.core.llamada_0800.llamada_0800 import SujetoDeLaConsulta, Pronombre, DefinicionLlamada, IntervecionSugerida
from src.core.schemas.como_ubico import como_ubico_schema, como_ubico_schema_many
from src.core.schemas.detalle_motivo_de_la_consulta import detalle_motivo_de_la_consulta_schema, detalle_motivos_de_la_consulta_schema
from src.core.schemas.motivo_de_la_consulta import motivo_de_la_consulta_schema, motivos_de_la_consulta_schema
from src.core.schemas.llamada_0800 import llamada_0800_schema, llamadas_0800_schema, observatorio_llamadas_0800_schema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
prueba_blueprint = Blueprint("prueba", __name__, url_prefix="/prueba")
auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
me_blueprint = Blueprint("me", __name__, url_prefix="/me")
user_blueprint = Blueprint("user", __name__, url_prefix="/users")
roles_blueprint = Blueprint("roles", __name__, url_prefix="/roles")
cetecsm_blueprint = Blueprint("cetecsm", __name__, url_prefix="/cetecsm")
observatorio_blueprint =  Blueprint("observatorio", __name__, url_prefix="/observatorio")
actividades_blueprint =  Blueprint("actividades", __name__, url_prefix="/actividades")
admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")

api_blueprint.register_blueprint(prueba_blueprint)
api_blueprint.register_blueprint(auth_blueprint)
api_blueprint.register_blueprint(me_blueprint)
api_blueprint.register_blueprint(user_blueprint)
api_blueprint.register_blueprint(roles_blueprint)
api_blueprint.register_blueprint(cetecsm_blueprint)
api_blueprint.register_blueprint(observatorio_blueprint)
api_blueprint.register_blueprint(actividades_blueprint)
api_blueprint.register_blueprint(admin_blueprint)

@prueba_blueprint.get("")
def get_all_pruebas():
    records = prueba.list_prueba()
    return jsonify(prueba_schema.dump(records))

@api_blueprint.post("auth")
def create_token():
    """Función que maneja el logueo del usuario y setea la cookie"""

    email = request.json.get("email", None)
    password = request.json.get("password", None)
    print(email)
    user = find_user_by_email(email)
    if user and (user.check_password(password)):
        access_token = create_access_token(identity=user.id)
        set_access_cookies(jsonify(), access_token)
        return jsonify({"token": access_token}), 200
    return jsonify({"msg": "Usuario o contraseña incorrecta"}), 401

@me_blueprint.get("profile")
@jwt_required()
def user_jwt():
    """Función que devuelve los datos de perfil del usuario"""
    current_user = get_jwt_identity()
    user = get_user(current_user)
    return make_response(jsonify(user_schema.dump(user))), 200


@api_blueprint.get("logout")
@jwt_required()
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200

@me_blueprint.get("/roles")
@jwt_required()
def get_user_roles():
    """ Función que devuelve los roles del usuario """
    current_user = get_jwt_identity()
    roles = get_roles(id=current_user)
    return make_response(jsonify(roles_schema.dump(roles))), 200

@user_blueprint.get("index")
@jwt_required()
def get_users():
    """ Función que devuelve el listado de usuarios registrados en el sistema en formato JSON """
    
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)
    users = list_users(page_num=page, per_page=per_page)
    if users:
        data = {
            "users": users_schema.dump(users),
            "page": page,
            "per_page": per_page,
            "total": users.total
        }
        return jsonify(data), 200
    else:
        return jsonify({"error": "No hay usuarios registrados en el sistema"}), 400

@user_blueprint.get("show/<int:id>")
#@jwt_required()
def get_user_by_id(id):
    """ Función que dado el id de un usuario registrado en el sistema, retorna la información del mismo """
    user = get_user(id=id)
    if user:
        user_data = user_schema.dump(user)
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 400



@user_blueprint.post("update/<int:id>")
@jwt_required()
def update_user(id):
    """ Función que permite a un usuario administrador actualizar los datos de otro usuario """    
    data = request.get_json()
    user = get_user(id=id)
    user.update(name=data['name'], last_name=data["lastName"], email=data["email"])
    update_roles(user, data['roles'])
    resp = make_response(jsonify({"msge": "Usuario actualizado exitosamente"}))
    return resp

@user_blueprint.post("create")
@jwt_required()
def register_user():
    """ Función que permite registrar un usuario """
    data = request.get_json()
    user = create_user(name=data['name'], last_name=data["lastName"], email=data["email"])
    update_roles(user, data['roles'])
    resp = make_response(jsonify({"msge": "Usuario registrado exitosamente."}))
    return resp

@roles_blueprint.get("index")
def get_index_roles():
    roles = list_roles()
    return make_response(jsonify(roles_schema.dump(roles))), 200

@cetecsm_blueprint.get("personas")
def get_personas_cetecsm_no_asignadas():

    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    personas_cetecsm = list_all_personas_cetecsm_no_asignadas(page_num=page, per_page=per_page)

    data = {
        "personas": personas_cetecsm_schemas.dump(personas_cetecsm),
        "page": page,
        "per_page": per_page,
        "total": personas_cetecsm.total
    }

    return make_response(jsonify(data)), 200

@api_blueprint.get("mot_grales_derivacion")
def get_index_motivos():
    mot_grales_derivacion = list_mot_gral_derivacion()
    return make_response(jsonify(mot_grales_deriv_schema.dump(mot_grales_derivacion))), 200

@cetecsm_blueprint.post("derivacion/create")
def create_derivation_cetecsm():
    data = request.get_json()
    derivacion = data['derivacion']
    persona = data['persona']
    persona_cetecsm = create_persona_cetecsm(
        dni=persona['dni'],
        dio_consentimiento=persona['dio_consentimiento'],
        municipio_id=persona['municipio'],
        nombre=persona['nombre'],
        apellido=persona['apellido'],
        edad=persona['edad'],
        telefono=persona['telefono'],
        telefono_alternativo=persona['telefono_alternativo']
    )

    nueva_derivacion = create_derivation(
        fecha=derivacion['fecha'], 
        dispositivo_derivacion=derivacion['dispositivo_derivacion'],
        nombre_operador_derivador=derivacion['nombre_operador_derivador'],
        descripcion=derivacion['descripcion'],
        persona_cetecsm_derivada=persona_cetecsm)
    
    print(derivacion['mot_gral_derivacion'])
    actualizar_derivacion(nueva_derivacion, derivacion['mot_gral_derivacion'])    

    resp = make_response(jsonify({"msge": "Derivación registrada exitosamente."}))
    return resp

@cetecsm_blueprint.post("asignarPersona/<int:persona_id>")
@jwt_required()
def asignar_persona_cetecsm(persona_id):
    current_user = get_jwt_identity()
    user = get_user(current_user)
    persona_cetecsm = get_persona_cetecsm(id=persona_id)
    asignar_persona(user, persona_cetecsm)
    persona_cetecsm.update(esta_activa=True)
    resp = make_response(jsonify({"msge": "Persona asignada exitosamente."}))
    return resp

@me_blueprint.get("personas_asignadas")
@jwt_required()
def get_personas_cetecsm_asignadas():
    current_user = get_jwt_identity()

    search_term = request.args.get("q", default="", type=str)
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    personas = get_personas_asignadas(search_term=search_term, page_num=page, per_page=per_page, user_id=current_user)
    
    data = {
        "personas": personas_cetecsm_schemas.dump(personas),
        "page": page,
        "per_page": per_page,
        "total": personas.total
    }
    
    return make_response(jsonify(data)), 200

@cetecsm_blueprint.get("persona/perfil/<int:id>")
def get_perfil_persona_cetecsm(id):
    persona_cetecsm = get_persona_cetecsm(id=id)

    if persona_cetecsm:
        return make_response(jsonify(persona_cetecsm_schemas.dump(persona_cetecsm))), 200
    else:
        return jsonify({"error": "Persona no encontrada"}), 400

@cetecsm_blueprint.get("persona/llamadas/<int:persona_id>")
def get_llamadas_recibidas(persona_id):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    llamadas_recibidas = list_llamadas_recibidas(page_num=page, per_page=per_page, persona_id=persona_id)

    data = {
        "llamadas": llamadas_cetecsm_schema.dump(llamadas_recibidas),
        "page": page,
        "per_page": per_page,
        "total": llamadas_recibidas.total
    }

    return make_response(jsonify(data)), 200

@cetecsm_blueprint.get("persona/llamadas/generar_sintesis/<int:persona_id>")
def get_archivo_sintesis(persona_id):

    buffer, error = generar_sintesis_detalles(persona_id=persona_id)
    
    if error:
        return jsonify({"error": error}), 400

    response = make_response(send_file(buffer, as_attachment=True, download_name='sintesis_llamadas.txt', mimetype='text/plain'))
    
    return response

@api_blueprint.get("municipios")
def get_index_municipios():
    municipios = list_municipios()
    return make_response(jsonify(municipios_schema.dump(municipios))), 200

@api_blueprint.get("regiones_sanitarias")
def get_index_regiones_sanitarias():
    regiones_sanitarias = list_regiones_sanitarias()
    return make_response(jsonify(regiones_sanitarias_schema.dump(regiones_sanitarias))), 200

@api_blueprint.get("grupos_convivientes")
def get_index_grupo_conviviente():
    grupos_convivientes = {grupo.name: grupo.value for grupo in GrupoConviviente}
    return make_response(jsonify(grupos_convivientes)), 200

@api_blueprint.get("resoluciones")
def get_index_resolucion():
    resoluciones = {resolucion.name: resolucion.value for resolucion in ResolucionLlamado}
    return make_response(jsonify(resoluciones)), 200

@api_blueprint.get("identidades_genero")
def get_index_identidad_genero():
    identidades_genero = list_identidades_genero()
    return make_response(jsonify(identidades_genero_schema.dump(identidades_genero))), 200

@api_blueprint.get("mot_grales_acomp")
def get_index_mot_gral_acomp():
    mot_grales_acomp = list_mot_gral_acomp()
    return make_response(jsonify(mot_grales_acomp_schema.dump(mot_grales_acomp))), 200

@api_blueprint.get("malestares_emocionales")
def get_index_malestar_emocional():
    malestares_emocionales = list_malestares_emocionales()
    return make_response(jsonify(malestares_emocionales_schema.dump(malestares_emocionales))), 200

@api_blueprint.get("situaciones_vulnerabilidad")
def get_index_situacion_vulnerabilidad():
    situaciones_vulnerabilidad = list_situaciones_vulnerabilidad()
    return make_response(jsonify(situaciones_vuln_schema.dump(situaciones_vulnerabilidad))), 200

@cetecsm_blueprint.post("persona/editar/<int:id>")
@jwt_required()
def editar_persona_cetecsm(id):
    """ Función que permite a un usuario administrador actualizar los datos de otro usuario """    
    data = request.get_json()
    persona = data['persona']
    persona_cetecsm = get_persona_cetecsm(id=id)
    persona_cetecsm.update(
        dni=persona['dni'], 
        grupo_conviviente=persona['grupo_conviviente'],
        grupo_conviviente_otro=persona['grupo_conviviente_otro'], 
        dio_consentimiento=persona['dio_consentimiento'],
        localidad=persona['localidad'],
        tiene_obra_social=persona['tiene_obra_social'],
        obra_social=persona['obra_social'],
        nombre=persona['nombre'],
        apellido=persona['apellido'],
        telefono=persona['telefono'],
        telefono_alternativo=persona['telefono_alternativo'],
        detalle_acompanamiento=persona['detalle_acompanamiento'],
        identidad_genero_id=persona['identidad_genero_id'],
        identidad_genero_otra=persona['identidad_genero_otra'],
        motivo_gral_acomp_id=persona['motivo_gral_acomp_id'],
        malestares_emocionales=persona['malestares_emocionales'],
        situaciones_vulnerabilidad=persona['situaciones_vulnerabilidad']
    )
    
    resp = make_response(jsonify({"msge": "Los datos de la persona fueron actualizados exitosamente"}))
    return resp

@cetecsm_blueprint.post("llamada/crear/<int:id>")
@jwt_required()
def crear_llamada_cetecsm(id):
    """ Función que permite a un usuario administrador actualizar los datos de otro usuario """
    current_user = get_jwt_identity()
    user = get_user(current_user)    
    data = request.get_json()
    persona = data['persona']
    llamada = data['llamada']

    if not llamada['resolucion'] == "Continua acompañamiento" and not llamada['resolucion'] == "Comunicación fallida":
        esta_activo = False
    else:
        esta_activo = True    

    persona_cetecsm = get_persona_cetecsm(id=id)
    persona_cetecsm.update( 
        grupo_conviviente=persona['grupo_conviviente'],
        grupo_conviviente_otro=persona['grupo_conviviente_otro'], 
        localidad=persona['localidad'],
        tiene_obra_social=persona['tiene_obra_social'],
        obra_social=persona['obra_social'],
        detalle_acompanamiento=persona['detalle_acompanamiento'],
        fecha_prox_llamado_actual=llamada['fecha_prox_llamado'],
        identidad_genero_id=persona['identidad_genero_id'],
        motivo_gral_acomp_id=persona['motivo_gral_acomp_id'],
        malestares_emocionales=persona['malestares_emocionales'],
        situaciones_vulnerabilidad=persona['situaciones_vulnerabilidad'],
        esta_activa=esta_activo
    )

    create_llamada_cetecsm(
        detalle=llamada['detalle'],
        resolucion=llamada['resolucion'],
        fecha_prox_llamado=llamada['fecha_prox_llamado'],
        usuario_carga=user,
        persona_cetecsm_llamada=persona_cetecsm
    )
    
    resp = make_response(jsonify({"msge": "Llamada cargada exitosamente"}))
    return resp

@cetecsm_blueprint.get("operadores")
def get_all_operadores_cetecsm():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    operadores_paginados = get_operadores_cetecsm(page=page, per_page=per_page)

    resultados = {
        "total": operadores_paginados.total,
        "page": operadores_paginados.page,
        "per_page": operadores_paginados.per_page,
        "items": [
            {
                "id": operador.id,
                "email": operador.email,
                "name": operador.name,
                "last_name": operador.last_name,
                "cantidad_personas_asignadas": operador.cantidad_personas_asignadas,
                "fecha_ultimo_llamado": operador.fecha_ultimo_llamado,
            }
            for operador in operadores_paginados.items
        ],
    }

    return make_response(jsonify(resultados))

@cetecsm_blueprint.get("personasAsignadas/<int:id>")
def get_asignaciones_operador(id):
    search_term = request.args.get("q", default="", type=str)
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    personas = get_personas_asignadas(search_term=search_term, page_num=page, per_page=per_page, user_id=id)

    for persona in personas.items:
        fecha_ultimo_llamado = obtener_fecha_ultimo_llamado(persona.id)

        persona.fecha_ultimo_llamado = fecha_ultimo_llamado

    data = {
        "personas": personas_cetecsm_schemas.dump(personas),
        "page": page,
        "per_page": per_page,
        "total": personas.total
    }
    
    return make_response(jsonify(data)), 200

@cetecsm_blueprint.get("asignadas_todas")
def personas_asignadas_index():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    personas = get_all_personas_asignadas(page_num=page, per_page=per_page)

    data = {
        "total": personas.total,
        "page": personas.page,
        "per_page": personas.per_page,
        "personas": [
            {
                "id": persona.id,
                "nombre": persona.nombre,
                "apellido": persona.apellido,
                "nombre_y_apellido_operador": f"{persona.usuario_asignado.name} {persona.usuario_asignado.last_name}",
                "cantidad_llamadas": obtener_cantidad_llamadas(persona.id),
                "resolucion_ultima_llamada": obtener_resolucion_ultima_llamada(persona.id),
            }
            for persona in personas.items
        ],
    }
    
    return make_response(jsonify(data)), 200

@observatorio_blueprint.get("personas_cetecsm_derivadas")
def obtener_personas_cetecsm_derivadas():
    regiones_sanitarias = request.args.get("regiones_seleccionadas", default="", type=str)
    dispositivo_derivador = request.args.get("dispositivo_derivador", default="", type=str)
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    edad_desde = request.args.get("edad_desde", default=None, type=int)
    edad_hasta = request.args.get("edad_hasta", default=None, type=int)
    mot_gral_derivacion = request.args.get("mot_gral_derivacion", default="", type=str)
    nombre_operador_derivador = request.args.get("nombre_operador_derivador", default="", type=str)
 
    search_terms = {
        "regiones_sanitarias": regiones_sanitarias.split(',') if regiones_sanitarias else [],
        "dispositivo_derivador": dispositivo_derivador,
        "fechas": {
            "desde": fecha_desde,
            "hasta": fecha_hasta
        },
        "edades": {
            "desde": edad_desde,
            "hasta": edad_hasta
        },
        "motivo_derivacion": mot_gral_derivacion,
        "operador": nombre_operador_derivador 
    }

    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)
    personas = get_personas_cetecsm_todas(search_terms=search_terms, page_num=page, per_page=per_page)

    items = {
        "personas": personas_cetecsm_schemas.dump(personas),
        "page": page,
        "per_page": per_page,
        "total": personas.total
    }

    return make_response(jsonify(items)), 200

@observatorio_blueprint.get("personas_cetecsm_derivadas/exportar")
def obtener_personas_cetecsm_derivadas_todas():
    regiones_sanitarias = request.args.get("regiones_seleccionadas", default="", type=str)
    dispositivo_derivador = request.args.get("dispositivo_derivador", default="", type=str)
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    edad_desde = request.args.get("edad_desde", default=None, type=int)
    edad_hasta = request.args.get("edad_hasta", default=None, type=int)
    mot_gral_derivacion = request.args.get("mot_gral_derivacion", default="", type=str)
    nombre_operador_derivador = request.args.get("nombre_operador_derivador", default="", type=str)
 
    search_terms = {
        "regiones_sanitarias": regiones_sanitarias.split(',') if regiones_sanitarias else [],
        "dispositivo_derivador": dispositivo_derivador,
        "fechas": {
            "desde": fecha_desde,
            "hasta": fecha_hasta
        },
        "edades": {
            "desde": edad_desde,
            "hasta": edad_hasta
        },
        "motivo_derivacion": mot_gral_derivacion,
        "operador": nombre_operador_derivador 
    }

    personas = get_personas_cetecsm_todas_sin_paginar(search_terms=search_terms)
    
    
    data = [{
        'fecha_derivacion': persona.derivacion.fecha,
        'dio_consentimiento': "Sí" if persona.dio_consentimiento else "No",
        'dispositivo_derivacion': persona.derivacion.dispositivo_derivacion,
        'nombre_operador_derivador': persona.derivacion.nombre_operador_derivador,
        'municipio': persona.municipio_id,
        'nombre': persona.nombre,
        'apellido': persona.apellido,
        'edad': persona.edad,
        'dni': persona.dni,
        'telefono': persona.telefono,
        'telefono_alternativo': persona.telefono_alternativo,
        'motivo_derivacion': persona.derivacion.tipo_motivo_gral,
        'otro_motivo_derivacion': persona.derivacion.mot_gral_derivacion.otro_tipo,
        'descripcion': persona.derivacion.descripcion,
        'grupo_conviviente': persona.grupo_conviviente,
        'localidad': persona.localidad,
        'identidad_genero': persona.identidad_genero_id,
        'obra_social': persona.obra_social,
        'motivo_acompañamiento': persona.motivo_gral_acomp_id,
        'tipo_malestar_emocional': ", ".join(persona.motivo_gral_acomp.malestares_emocionales) if persona.motivo_gral_acomp else None,
        'detalle_acompanamiento': persona.detalle_acompanamiento,
        'fecha_prox_llamado': persona.fecha_prox_llamado_actual
    } for persona in personas]

    return convert_to_csv(data, "personas_derivadas.csv")
    
@observatorio_blueprint.get("personas_cetecsm_seguimiento")
def obtener_informacion_personas_seguimiento_todas():
    regiones_sanitarias = request.args.get("regiones_seleccionadas", default="", type=str)
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    edad_desde = request.args.get("edad_desde", default=None, type=int)
    edad_hasta = request.args.get("edad_hasta", default=None, type=int)
    identidad_genero = request.args.get("identidad_genero", default="", type=str)
    mot_gral_acomp = request.args.get("mot_gral_acomp", default="", type=str)
    
    search_terms = {
        "regiones_sanitarias": regiones_sanitarias.split(',') if regiones_sanitarias else [],
        "fechas": {
            "desde": fecha_desde,
            "hasta": fecha_hasta
        },
        "edades": {
            "desde": edad_desde,
            "hasta": edad_hasta
        },
        "identidad_genero": identidad_genero,
        "mot_gral_acomp": mot_gral_acomp,
    }

    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    personas = obtener_informacion_personas_seguimiento(search_terms=search_terms ,page_num=page, per_page=per_page)

    datos_personas = []
    for persona in personas:
        resolucion_primera_llamada, fecha_primera_llamada, resolucion_ultima_llamada = obtener_datos_resolucion_fecha_llamada(persona)
        datos_persona = {
            "region_sanitaria": persona.municipio.region_sanitaria.tipo,
            "edad": persona.edad,
            "identidad_genero": persona.identidad_genero_id,
            "motivo_acompanamiento": persona.motivo_gral_acomp_id,
            "tipo_malestar_emocional": persona.malestares_emocionales if persona.motivo_gral_acomp_id == "Malestar emocional" else None,
            "resolucion_primera_llamada": resolucion_primera_llamada,
            "fecha_primera_llamada": fecha_primera_llamada.strftime("%Y-%m-%d"),
            "resolucion_ultima_llamada": resolucion_ultima_llamada,
        }
        datos_personas.append(datos_persona)

    data = {
        "personas": datos_personas,
        "page": page,
        "per_page": per_page,
        "total": personas.total
    }

    # Devolver los resultados como JSON
    return make_response(jsonify(data))

@observatorio_blueprint.get("personas_cetecsm_seguimiento/exportar")
def obtener_personas_cetecsm_asignadas_exportar():
    regiones_sanitarias = request.args.get("regiones_seleccionadas", default="", type=str)
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    edad_desde = request.args.get("edad_desde", default=None, type=int)
    edad_hasta = request.args.get("edad_hasta", default=None, type=int)
    identidad_genero = request.args.get("identidad_genero", default="", type=str)
    mot_gral_acomp = request.args.get("mot_gral_acomp", default="", type=str)
    
    search_terms = {
        "regiones_sanitarias": regiones_sanitarias.split(',') if regiones_sanitarias else [],
        "fechas": {
            "desde": fecha_desde,
            "hasta": fecha_hasta
        },
        "edades": {
            "desde": edad_desde,
            "hasta": edad_hasta
        },
        "identidad_genero": identidad_genero,
        "mot_gral_acomp": mot_gral_acomp,
    }

    personas = obtener_informacion_personas_seguimiento(search_terms=search_terms, debe_paginarse=False)
    
    
    data = [{
        'fecha_derivacion': persona.derivacion.fecha,
        'dio_consentimiento': "Sí" if persona.dio_consentimiento else "No",
        'dispositivo_derivacion': persona.derivacion.dispositivo_derivacion,
        'nombre_operador_derivador': persona.derivacion.nombre_operador_derivador,
        'municipio': persona.municipio_id,
        'nombre': persona.nombre,
        'apellido': persona.apellido,
        'edad': persona.edad,
        'dni': persona.dni,
        'telefono': persona.telefono,
        'telefono_alternativo': persona.telefono_alternativo,
        'motivo_derivacion': persona.derivacion.tipo_motivo_gral,
        'otro_motivo_derivacion': persona.derivacion.mot_gral_derivacion.otro_tipo,
        'descripcion': persona.derivacion.descripcion,
        'grupo_conviviente': persona.grupo_conviviente,
        'localidad': persona.localidad,
        'identidad_genero': persona.identidad_genero_id,
        'obra_social': persona.obra_social,
        'motivo_acompañamiento': persona.motivo_gral_acomp_id,
        'tipo_malestar_emocional': persona.malestares_emocionales if persona.motivo_gral_acomp_id else None,
        'detalle_acompanamiento': persona.detalle_acompanamiento,
        'fecha_prox_llamado': persona.fecha_prox_llamado_actual
    } for persona in personas]

    return convert_to_csv(data, "personas_en_seguimiento.csv")

@observatorio_blueprint.get("cantidad_llamadas")
def obtener_cantidad_llamadas_todas():
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    usuario_id = request.args.get("usuario_id", default=None, type=int)
    resolucion = request.args.get("resolucion_llamado", default=None, type=str)

    total_llamados_cetecsm = obtener_total_llamados_cetecsm(fecha_desde=fecha_desde, fecha_hasta=fecha_hasta, usuario_id=usuario_id, resolucion=resolucion)

    return make_response(jsonify({"total_llamados": total_llamados_cetecsm}))

@observatorio_blueprint.get("llamadas_0800")
def obtener_llamadas_0800_observatorio():
    regiones_sanitarias = request.args.get("regiones_seleccionadas", default="", type=str)
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    edad_desde = request.args.get("edad_desde", default=None, type=int)
    edad_hasta = request.args.get("edad_hasta", default=None, type=int)
    motivo_consulta = request.args.get("motivo_consulta", default="", type=str)
    detalle_motivo_consulta = request.args.get("detalle_motivo_consulta", default="", type=str)
    genero = request.args.get('genero', default='', type=str)
 
    search_terms = {
        "regiones_sanitarias": regiones_sanitarias.split(',') if regiones_sanitarias else [],
        "fechas": {
            "desde": fecha_desde,
            "hasta": fecha_hasta
        },
        "edades": {
            "desde": edad_desde,
            "hasta": edad_hasta
        },
        "motivo_consulta": motivo_consulta,
        "detalle_motivo_consulta": detalle_motivo_consulta,
        'genero': genero 
    }

    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)
    llamadas = get_llamadas_0800_todas(search_terms=search_terms, page_num=page, per_page=per_page)

    items = {
        "llamadas": observatorio_llamadas_0800_schema.dump(llamadas),
        "page": page,
        "per_page": per_page,
        "total": llamadas.total
    }

    return make_response(jsonify(items)), 200

@observatorio_blueprint.get("llamadas_0800/exportar")
def obtener_llamadas_0800_observatorio_exportar():
    regiones_sanitarias = request.args.get("regiones_seleccionadas", default="", type=str)
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    edad_desde = request.args.get("edad_desde", default=None, type=int)
    edad_hasta = request.args.get("edad_hasta", default=None, type=int)
    motivo_consulta = request.args.get("motivo_consulta", default="", type=str)
    detalle_motivo_consulta = request.args.get("detalle_motivo_consulta", default="", type=str)
    genero = request.args.get('genero', default='', type=str)
 
    search_terms = {
        "regiones_sanitarias": regiones_sanitarias.split(',') if regiones_sanitarias else [],
        "fechas": {
            "desde": fecha_desde,
            "hasta": fecha_hasta
        },
        "edades": {
            "desde": edad_desde,
            "hasta": edad_hasta
        },
        "motivo_consulta": motivo_consulta,
        "detalle_motivo_consulta": detalle_motivo_consulta,
        'genero': genero 
    }

    llamadas = get_llamadas_0800_todas_sin_paginar(search_terms=search_terms)
    
    data = [{
        'email_operador': llamada.email_operador,
        'motivo_consulta': llamada.motivo_nombre,
        'como_ubico': llamada.como_ubico_forma,
        'como_ubico_otro': llamada.como_ubico_otro,
        'municipio': llamada.municipio,
        'sujeto': llamada.sujeto,
        'edad': llamada.edad,
        'identidad_genero': llamada.identidad_genero_tipo,
        'pronombre': llamada.pronombre,
        'grupo_conviviente': llamada.grupo_conviviente,
        'grupo_conviviente_otro': llamada.grupo_conviviente_otro,
        'detalle_motivo_consulta': llamada.detalle_motivo_motivo,
        'malestares_emocionales': llamada.malestares_emocionales,
        'malestares_emocionales_otro': llamada.malestares_emocionales_otro,
        'situaciones_vulnerabilidad': llamada.situaciones_vulnerabilidad,
        'definicion_llamado': llamada.definicion,
        'intervencion_sugerida': llamada.intervencion_sugerida,
        'motivo_derivacion': llamada.motivo_derivacion,
        'motivo_derivacion_otro': llamada.motivo_derivacion_otro,
        'nombre': llamada.nombre,
        'apellido': llamada.apellido,
        'dni': llamada.dni,
        'telefonos': llamada.telefonos,
        'emails': llamada.emails,
        'domicilio': llamada.domicilio,
        'nacionalidad': llamada.nacionalidad,
        'nacimiento': llamada.nacimiento,
        'detalle_intervencion': llamada.detalle_intervencion,
        'duracion': llamada.duracion,
        'demanda_tratamiento': "Sí" if llamada.demanda_tratamiento else "No",
        'fecha_y_hora_carga': llamada.fecha_y_hora_carga
    } for llamada in llamadas]

    return convert_to_csv(data, "llamadas_0800.csv")

@cetecsm_blueprint.get("operadores_cetecsm")
def obtener_operadores_cetecsm():

    operadores_cetecsm = obtener_usuario_por_rol(rol="Operador CETECSM")
    return make_response(jsonify(users_schema.dump(operadores_cetecsm)))

@actividades_blueprint.get("talleres")
def obtener_talleres_actividades():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)
    tipo_actividad = request.args.get("tipo_taller", default="", type=str)

    talleres = get_talleres(tipo_actividad=tipo_actividad, page=page, per_page=per_page)

    data = {
        "talleres": talleres_schema.dump(talleres),
        "page": page,
        "per_page": per_page,
        "total": talleres.total
    }

    return make_response(jsonify(data))

@actividades_blueprint.get("tipos_taller")
def get_index_tipo_talleres():
    tipo_talleres = {tipo.name: tipo.value for tipo in TiposActividades}
    return make_response(jsonify(tipo_talleres)), 200

@actividades_blueprint.get("dispositivos")
def get_index_dispositivos():
    dispositivos = list_dispositivos()
    return make_response(jsonify(dispositivos_schema.dump(dispositivos))), 200

@actividades_blueprint.get("años")
def get_index_años():
    años = {año.name: año.value for año in Anios}
    return make_response(jsonify(años)), 200

@actividades_blueprint.get("divisiones")
def get_index_divisiones():
    divisiones = {division.name: division.value for division in Divisiones}
    return make_response(jsonify(divisiones)), 200

@actividades_blueprint.get("actividades_internas")
def get_index_actividades_internas():
    actividades_internas = list_actividades_internas()
    return make_response(jsonify(actividades_internas_schema.dump(actividades_internas)))

@actividades_blueprint.get("actividades_externas")
def get_index_actividades_externas():
    actividades_externas = list_actividades_externas()
    return make_response(jsonify(actividades_externas_schema.dump(actividades_externas)))

@actividades_blueprint.get("escuelas")
def get_index_escuelas():
    municipio = request.args.get("municipio", default="", type=str)
    escuelas = get_escuelas_by_municipio(municipio)
    return make_response(jsonify(escuelas_schema.dump(escuelas)))

@actividades_blueprint.get("localidades")
def get_index_localidades():
    municipio = request.args.get("municipio", default="", type=str)
    localidades = get_localidades_by_municipio(municipio)
    return make_response(jsonify(localidades_schema.dump(localidades)))

@actividades_blueprint.post("registrar_taller")
@jwt_required()
def registrar_taller():
    current_user = get_jwt_identity()
    data = request.get_json()
    actividad = data['actividad']
    taller = data['taller']
    
    if actividad['tipo'] == 'Talleres de Salud Mental en las Escuelas':
        escuela = data['escuela']
        años = []
        for año in actividad['anios']:
            anio = create_anio(anio=año['anio'], divisiones=", ".join(año['divisiones']))
            años.append(anio)

        act = create_actividad(
            cant_participantes=actividad['cant_participantes'],
            observaciones=actividad['observaciones'],
            cant_encuentros=actividad['cant_encuentros'],
            escuela_cue=escuela['cue'],
            anios=años,
        )

    else:
        print('aca estoy :/')
        print(actividad)
        act = create_actividad(
            cant_participantes=actividad['cant_participantes'],
            observaciones=actividad['observaciones'],
            actividad=str(actividad['actividades'])
        )
    
    create_taller(
        tipo=actividad['tipo'],
        municipio_id=taller['municipio']['nombre'],
        localidad=taller['localidad'],
        dispositivo_id=taller['dispositivo'],
        usuario_id=current_user,
        actividad=act
    )

    resp = make_response(jsonify({"msge": "Taller cargado exitosamente"}))
    return resp

@actividades_blueprint.get("estadisticas")
def get_estadisticas():
    tipo_taller = request.args.get("tipo_taller", default="Talleres de Salud Mental en las Escuelas", type=str)
    parametro_agrupacion = request.args.get("param_agrupacion", default="Año", type=str)
    tipo_actividad = request.args.get("tipo_actividad", default="Todas", type=str)
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    dict_params = {'Año': 'fecha_hora_carga','Municipio': 'municipio_id', 'Región sanitaria': 'region_sanitaria_id', 'Dispositivo': 'dispositivo_id'}

    estadisticas = obtener_estadisticas(tipo_taller, dict_params[parametro_agrupacion], tipo_actividad, page, per_page)
    lista = []

    for estadistica in estadisticas:
        data_estadisticas = {
            'agrupado_por': getattr(estadistica, dict_params[parametro_agrupacion]),
            'cantidad_talleres': estadistica.cant_talleres,
            'cantidad_encuentros': estadistica.cant_encuentros,
            'cantidad_escuelas': estadistica.cant_escuelas,
            'cantidad_participantes': estadistica.cant_participantes
        }
        lista.append(data_estadisticas)
    
    data = {
        'estadisticas': lista,
        'page': page,
        'per_page': per_page,
        'total': estadisticas.total
    }

    return make_response(jsonify(data))

# Api para la parte del 0800

@api_blueprint.get("sujetos_consulta")
def get_index_sujeto_consulta():
    sujetos_consulta = {sujeto.name: sujeto.value for sujeto in SujetoDeLaConsulta}
    return make_response(jsonify(sujetos_consulta)), 200

@api_blueprint.get("pronombres")
def get_index_pronombres():
    pronombres = {pronombre.name: pronombre.value for pronombre in Pronombre}
    return make_response(jsonify(pronombres)), 200

@api_blueprint.get("definiciones_llamada_0800")
def get_index_definiciones_llamada():
    definiciones = {definicion.name: definicion.value for definicion in DefinicionLlamada}
    return make_response(jsonify(definiciones)), 200

@api_blueprint.get("intervenciones_sugeridas")
def get_index_intervenciones_sugeridas():
    intervenciones = {intervencion.name: intervencion.value for intervencion in IntervecionSugerida}
    return make_response(jsonify(intervenciones)), 200

@api_blueprint.get("motivos_consulta")
def get_index_motivos_consulta():
    motivos = list_motivos_consulta()
    return make_response(jsonify(motivos_de_la_consulta_schema.dump(motivos))), 200

@api_blueprint.get("como_ubico")
def get_index_como_ubico():
    formas = list_como_ubico()
    return make_response(jsonify(como_ubico_schema_many.dump(formas))), 200

@api_blueprint.get("detalle_motivos_consulta")
def get_index_detalle_motivos_consulta():
    motivos = list_detalles_motivo_consulta()
    return make_response(jsonify(detalle_motivos_de_la_consulta_schema.dump(motivos))), 200

@api_blueprint.post("llamada_0800/crear")
@jwt_required()
def crear_llamada_0800():
    """ Función que permite a un usuario Operador del 0800 cargar una llamada """
    # current_user = get_jwt_identity()
    # user = get_user(current_user)
    data = request.get_json()
    llamada = data['llamada']
    print(llamada)

    if llamada['definicion'] == 'Derivación a CETEC SM':

        # Obtengo los teléfonos de la persona
        telefonos: list = json.loads(llamada['telefonos'])
        print(telefonos)
        if len(telefonos) > 0:
            telefono = telefonos[0]['numero']
            if len(telefonos) > 1:
                telefono_secundario = telefonos[1]['numero']
            else:
                telefono_secundario = ''
        else:
            telefono = ''
            telefono_secundario = ''

        persona_cetecsm = create_persona_cetecsm(
            dni=llamada['dni'],
            dio_consentimiento=llamada['demanda_tratamiento'],
            municipio=get_by_name(llamada['municipio']),
            nombre=llamada['nombre'],
            apellido=llamada['apellido'],
            edad=llamada['edad'],
            telefono=telefono,
            telefono_alternativo=telefono_secundario
        )

        nueva_derivacion = create_derivation(
            dispositivo_derivacion='0800',
            nombre_operador_derivador=llamada['email_operador'],
            descripcion=llamada['detalle'],
            persona_cetecsm_derivada=persona_cetecsm)

        # Formateo el motivo para que funcione bien
        motivo_derivacion = {'tipo':llamada['motivo_derivacion'], 'otro_tipo':llamada['motivo_derivacion_otro']}
        
        actualizar_derivacion(nueva_derivacion, motivo_derivacion)
    
    persona_cetecsm_id = persona_cetecsm.id if (llamada['definicion'] == 'Derivación a CETEC SM') else ''

    create_llamada_0800(
        motivo_nombre = llamada['motivo_consulta'],
        como_ubico_forma = llamada['como_ubico'],
        como_ubico_otro = llamada['como_ubico_otro'],
        municipio_nombre = llamada['municipio'],
        sujeto = llamada['sujeto'],
        edad = llamada['edad'],
        identidad_genero_tipo = llamada['identidad_genero'],
        identidad_genero_otra = llamada['identidad_genero_otra'],
        pronombre = llamada['pronombre'],
        grupo_conviviente = llamada['grupo_conviviente'],
        grupo_conviviente_otro = llamada['grupo_conviviente_otro'],
        detalle_motivo_motivo = llamada['detalle_motivo_consulta'],
        malestares_emocionales = llamada['malestares_emocionales'],
        malestares_emocionales_otro = llamada['malestares_emocionales_otro'],
        situaciones_vulnerabilidad = llamada['situaciones_vulnerabilidad'],
        definicion = llamada['definicion'],
        persona_cetecsm_id = persona_cetecsm_id,
        intervencion_sugerida = llamada['intervencion_sugerida'],
        motivo_derivacion = llamada['motivo_derivacion'],
        motivo_derivacion_otro = llamada['motivo_derivacion_otro'],
        nombre = llamada['nombre'],
        apellido = llamada['apellido'],
        dni = llamada['dni'],
        telefonos = llamada['telefonos'],
        emails = llamada['emails'],
        domicilio = llamada['domicilio'],
        nacionalidad = llamada['nacionalidad'],
        nacimiento = llamada['nacimiento'],
        detalle_intervencion = llamada['detalle'],
        duracion = llamada['duracion'],
        demanda_tratamiento = llamada['demanda_tratamiento'],
        email_operador = llamada['email_operador']
    )
    
    resp = make_response(jsonify({"msge": "Llamada cargada exitosamente"}))
    return resp

@api_blueprint.get("0800/llamadas")
def get_llamadas_0800():

    search_term = request.args.get("q", default="", type=str)
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    llamadas_0800 = list_llamadas_0800(search_term=search_term, page_num=page, per_page=per_page)

    data = {
        "llamadas": llamadas_0800_schema.dump(llamadas_0800),
        "page": page,
        "per_page": per_page,
        "total": llamadas_0800.total
    }

    return make_response(jsonify(data)), 200

@api_blueprint.get("0800/verSeguimiento/<int:llamada_id>")
def ver_seguimiento(llamada_id):
    llamada = get_llamada_0800_by_id(llamada_id)
    persona_cetecsm = get_persona_cetecsm(llamada.persona_cetecsm_id)
    if persona_cetecsm.esta_asignada:
        operador_cetecsm = get_user(persona_cetecsm.usuario_id)
        nom_y_ape = operador_cetecsm.name + ' ' + operador_cetecsm.last_name
        return make_response(jsonify({
            'esta_asignada': True,
            'fecha_ult_llamado': obtener_fecha_ultimo_llamado(persona_cetecsm.id),
            'operador': nom_y_ape
        })), 200
    else:
        return make_response(jsonify({
            'esta_asignada': False
        })), 200

@admin_blueprint.get("opciones/<string:opcion>")
def get_opciones(opcion):
    match opcion:
        case 'motivos_consulta':
            opciones = [opcion['nombre'] for opcion in motivos_de_la_consulta_schema.dump(list_motivos_consulta())]
        case 'como_ubico':
            opciones = [opcion['forma'] for opcion in como_ubico_schema_many.dump(list_como_ubico())]
        case 'generos':
            opciones = [opcion['tipo'] for opcion in identidades_genero_schema.dump(list_identidades_genero())]
        case 'detalles_motivo_consulta':
            opciones = [opcion['motivo'] for opcion in detalle_motivos_de_la_consulta_schema.dump(list_detalles_motivo_consulta())]
        case 'malestares_emocionales':
            opciones = [opcion['tipo'] for opcion in malestares_emocionales_schema.dump(list_malestares_emocionales())]
        case 'situaciones_vulnerabilidad':
            opciones = [opcion['tipo'] for opcion in situaciones_vuln_schema.dump(list_situaciones_vulnerabilidad())]
        case 'localidades':
            opciones = [opcion['nombre'] for opcion in localidades_schema.dump(list_localidades())]
        case 'motivos_acompanamiento':
            opciones = [opcion['tipo'] for opcion in mot_grales_acomp_schema.dump(list_mot_gral_acomp())]
        case 'dispositivos':
            opciones = [opcion['nombre'] for opcion in dispositivos_schema.dump(list_dispositivos())]
        case 'actividades_internas':
            opciones = [opcion['nombre'] for opcion in actividades_internas_schema.dump(list_actividades_internas())]
        case 'actividades_externas':
            opciones = [opcion['nombre'] for opcion in actividades_externas_schema.dump(list_actividades_externas())]
    return make_response(jsonify(opciones)), 200

@admin_blueprint.post("guardar-opciones")
def save_opciones():
    opcion = request.get_json()['opcion']
    opciones = json.loads(request.get_json()['opciones'])
    match opcion:
        case 'motivos_consulta':
            vaciar_motivos_consulta()
            for opcion in opciones:
                create_motivo_consulta(nombre=opcion)
        case 'como_ubico':
            vaciar_como_ubico()
            for opcion in opciones:
                create_como_ubico(forma=opcion)
        case 'generos':
            vaciar_identidad_genero()
            for opcion in opciones:
                create_identidad_genero(tipo=opcion)
        case 'detalles_motivo_consulta':
            vaciar_detalles_motivo_consulta()
            for opcion in opciones:
                create_detalle_motivo_consulta(motivo=opcion)
        case 'malestares_emocionales':
            vaciar_malestares_emocionales()
            for opcion in opciones:
                create_malestar_emocional(tipo=opcion)
        case 'situaciones_vulnerabilidad':
            vaciar_situaciones_vulnerabilidad()
            for opcion in opciones:
                create_situacion_vulnerabilidad(tipo=opcion)
        case 'localidades':
            vaciar_localidades()
            for opcion in opciones:
                create_localidad(nombre=opcion)
        case 'motivos_acompanamiento':
            vaciar_mot_gral_acomp()
            for opcion in opciones:
                create_mot_gral_acomp(tipo=opcion)
        case 'dispositivos':
            vaciar_dispositivos()
            for opcion in opciones:
                create_dispositivo(nombre=opcion)
        case 'actividades_internas':
            vaciar_acctividades_internas()
            for opcion in opciones:
                create_actividad_interna(nombre=opcion)
        case 'actividades_externas':
            vaciar_acctividades_externas()
            for opcion in opciones:
                create_actividad_externa(nombre=opcion)
    return make_response(), 200

@observatorio_blueprint.get("talleres")
def obtener_talleres_observatorio():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)
    regiones_sanitarias = request.args.get("regiones_sanitarias", default="", type=str)
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    municipio = request.args.get("municipio", default="", type=str)
    gestion = request.args.get("gestion", default="", type=str)
 
    search_terms = {
        "regiones_sanitarias": regiones_sanitarias.split(',') if regiones_sanitarias else [],
        "fechas": {
            "desde": fecha_desde,
            "hasta": fecha_hasta
        },
        "municipio": municipio,
        "gestion": gestion
    }

    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)
    talleres = get_talleres_escuelas_todos(search_terms=search_terms, page_num=page, per_page=per_page)

    data = {
        "talleres": talleres_schema_observatorio.dump(talleres),
        "page": page,
        "per_page": per_page,
        "total": talleres.total
    }

    return make_response(jsonify(data))

@observatorio_blueprint.get("gestiones")
def get_index_gestiones():
    gestiones = {gestion.name: gestion.value for gestion in Sectores}
    return make_response(jsonify(gestiones)), 200

@observatorio_blueprint.get("talleres/exportar")
def obtener_talleres_observatorio_exportar():
    regiones_sanitarias = request.args.get("regiones_sanitarias", default="", type=str)
    fecha_desde = request.args.get("fecha_desde", default=None, type=str)
    fecha_hasta = request.args.get("fecha_hasta", default=None, type=str)
    municipio = request.args.get("municipio", default="", type=str)
    gestion = request.args.get("gestion", default="", type=str)
 
    search_terms = {
        "regiones_sanitarias": regiones_sanitarias.split(',') if regiones_sanitarias else [],
        "fechas": {
            "desde": fecha_desde,
            "hasta": fecha_hasta
        },
        "municipio": municipio,
        "gestion": gestion
    }

    talleres = get_talleres_escuelas_todos_sin_paginar(search_terms=search_terms)

    def obtener_anios_trabajados(taller):
        aniosTrabajados = ''
        for anio in taller.actividad.anios:
            aniosTrabajados += f'{anio.anio}({anio.divisiones}), '
        return aniosTrabajados[:-2]
    
    data = [{
        'localidad': taller.localidad,
        'municipio': taller.municipio_id,
        'region_sanitaria': taller.municipio.region_sanitaria.tipo,
        'dispositivo': taller.dispositivo_id,
        'nombre_escuela': taller.actividad.escuela.nombre if taller.actividad.escuela else "",
        'cue_escuela': taller.actividad.escuela_cue,
        'años_trabajados': obtener_anios_trabajados(taller),
        'cantidad_encuentros': taller.actividad.cant_encuentros,
        'cantidad_participantes': taller.actividad.cant_participantes,
        'observaciones': taller.actividad.observaciones
    } for taller in talleres]

    return convert_to_csv(data, "llamadas_0800.csv")