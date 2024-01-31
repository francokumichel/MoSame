import json
from flask import (
    Blueprint,
    jsonify,
    make_response,
    request,
)

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)

from src.core.permissions import list_roles
from src.core.users import find_user_by_email, get_user, create_user, get_roles, update_roles, list_users, asignar_persona, get_personas_asignadas
from src.core.schemas.user import user_schema, users_schema
from src.core.persona_cetecsm import create_persona_cetecsm, list_personas_cetecsm, get_persona_cetecsm, list_llamadas_recibidas, actualizar_identidad_genero, actualizar_mot_gral_acomp, actualizar_sit_vuln, list_municipios
from src.core.schemas.persona_cetecsm import persona_cetecsm_schemas, personas_cetecsm_schemas
from src.core.schemas.municipio import municipios_schema
from src.core.schemas.role import roles_schema
from src.core.derivacion import actualizar_derivacion
from src.core.motivo_general_derivacion import list_mot_gral_derivacion
from src.core.schemas.motivo_general_derivacion import mot_grales_deriv_schema
from src.core.derivacion import create_derivation
from src.core.llamada_cetecsm import create_llamada_cetecsm
from src.core.llamada_cetecsm.llamada_cetecsm import ResolucionLlamado
from src.core.schemas.llamada_cetecsm import llamadas_cetecsm_schema
from src.core import prueba
from src.core.schemas.prueba import prueba_schema
from src.core.motivo_general_acompanamiento import list_mot_gral_acomp
from src.core.schemas.motivo_general_acompanamiento import mot_grales_acomp_schema
from src.core.persona_cetecsm.persona_cetecsm import GrupoConviviente
from src.core.identidad_genero import list_identidades_genero
from src.core.schemas.identidad_genero import identidades_genero_schema
from src.core.malestar_emocional import list_malestares_emocionales
from src.core.schemas.malestar_emocional import malestares_emocionales_schema
from src.core.situaciones_vulnerabilidad import list_situaciones_vulnerabilidad
from src.core.schemas.situacion_vulnerabilidad import situaciones_vuln_schema
from src.core.llamada_0800 import list_como_ubico, list_detalles_motivo_consulta, list_llamadas_0800, list_motivos_consulta, create_llamada_0800
from src.core.llamada_0800.llamada_0800 import SujetoDeLaConsulta, Pronombre, DefinicionLlamada, IntervecionSugerida
from src.core.schemas.como_ubico import como_ubico_schema, como_ubico_schema_many
from src.core.schemas.detalle_motivo_de_la_consulta import detalle_motivo_de_la_consulta_schema, detalle_motivos_de_la_consulta_schema
from src.core.schemas.motivo_de_la_consulta import motivo_de_la_consulta_schema, motivos_de_la_consulta_schema
from src.core.schemas.llamada_0800 import llamada_0800_schema, llamadas_0800_schema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
prueba_blueprint = Blueprint("prueba", __name__, url_prefix="/prueba")
auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
me_blueprint = Blueprint("me", __name__, url_prefix="/me")
user_blueprint = Blueprint("user", __name__, url_prefix="/users")
roles_blueprint = Blueprint("roles", __name__, url_prefix="/roles")
cetecsm_blueprint = Blueprint("cetecsm", __name__, url_prefix="/cetecsm") 

api_blueprint.register_blueprint(prueba_blueprint)
api_blueprint.register_blueprint(auth_blueprint)
api_blueprint.register_blueprint(me_blueprint)
api_blueprint.register_blueprint(user_blueprint)
api_blueprint.register_blueprint(roles_blueprint)
api_blueprint.register_blueprint(cetecsm_blueprint)


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
    return user_schema.dump(user), 200


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
    resp.headers["Content-Type: application/json"] = "*"
    return resp

@user_blueprint.post("create")
@jwt_required()
def register_user():
    """ Función que permite registrar un usuario """
    data = request.get_json()
    user = create_user(name=data['name'], last_name=data["lastName"], email=data["email"])
    update_roles(user, data['roles'])
    resp = make_response(jsonify({"msge": "Usuario registrado exitosamente."}))
    resp.headers["Content-Type: application/json"] = "*"
    return resp

@roles_blueprint.get("index")
def get_index_roles():
    roles = list_roles()
    return make_response(jsonify(roles_schema.dump(roles))), 200

@cetecsm_blueprint.get("personas")
def get_personas_cetecsm():

    search_term = request.args.get("q", default="", type=str)
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=1, type=int)

    personas_cetecsm = list_personas_cetecsm(search_term=search_term, page_num=page, per_page=per_page)

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
    resp.headers["Content-Type: application/json"] = "*"
    return resp

@cetecsm_blueprint.post("asignarPersona/<int:persona_id>")
@jwt_required()
def asignar_persona_cetecsm(persona_id):
    current_user = get_jwt_identity()
    user = get_user(current_user)
    persona_cetecsm = get_persona_cetecsm(id=persona_id)
    asignar_persona(user, persona_cetecsm)
    resp = make_response(jsonify({"msge": "Persona asignada exitosamente."}))
    resp.headers["Content-Type: application/json"] = "*"
    return resp

@me_blueprint.get("personasAsignadas")
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

@api_blueprint.get("municipios")
def get_index_municipios():
    municipios = list_municipios()
    return make_response(jsonify(municipios_schema.dump(municipios))), 200

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
    print(persona)
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
    )

    actualizar_identidad_genero(persona=persona_cetecsm, identidad_genero=persona['identidad_genero'])
    actualizar_mot_gral_acomp(persona=persona_cetecsm, mot_gral_acomp=persona['motivo_gral_acomp'])
    actualizar_sit_vuln(persona=persona_cetecsm, situaciones_vulnerabilidad=persona['situaciones_vulnerabilidad'])

    
    resp = make_response(jsonify({"msge": "Los datos de la persona fueron actualizados exitosamente"}))
    resp.headers["Content-Type: application/json"] = "*"
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
    print(persona)
    persona_cetecsm = get_persona_cetecsm(id=id)
    persona_cetecsm.update( 
        grupo_conviviente=persona['grupo_conviviente'],
        grupo_conviviente_otro=persona['grupo_conviviente_otro'], 
        localidad=persona['localidad'],
        tiene_obra_social=persona['tiene_obra_social'],
        obra_social=persona['obra_social'],
        detalle_acompanamiento=persona['detalle_acompanamiento'],
        fecha_prox_llamado_actual=llamada['fecha_prox_llamado']
    )

    actualizar_identidad_genero(persona=persona_cetecsm, identidad_genero=persona['identidad_genero'])
    actualizar_mot_gral_acomp(persona=persona_cetecsm, mot_gral_acomp=persona['motivo_gral_acomp'])
    actualizar_sit_vuln(persona=persona_cetecsm, situaciones_vulnerabilidad=persona['situaciones_vulnerabilidad'])

    create_llamada_cetecsm(
        detalle=llamada['detalle'],
        resolucion=llamada['resolucion'],
        fecha_prox_llamado=llamada['fecha_prox_llamado'],
        usuario_carga=user,
        persona_cetecsm_llamada=persona_cetecsm
    )
    
    resp = make_response(jsonify({"msge": "Llamada cargada exitosamente"}))
    resp.headers["Content-Type: application/json"] = "*"
    return resp

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
# @jwt_required()
def crear_llamada_0800():
    """ Función que permite a un usuario Operador del 0800 cargar una llamada """
    # current_user = get_jwt_identity()
    # user = get_user(current_user)
    data = request.get_json()
    llamada = data['llamada']
    print(llamada)

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
            municipio_id=llamada['municipio'],
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
    
    resp = make_response(jsonify({"msge": "Llamada cargada exitosamente"}))
    resp.headers["Content-Type: application/json"] = "*"
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