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
from src.core.users import find_user_by_email, get_user, create_user, get_roles, update_roles, list_users
from src.core.schemas.user import user_schema, users_schema
from src.core.schemas.role import roles_schema

from src.core import prueba
from src.core.schemas.prueba import prueba_schema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
prueba_blueprint = Blueprint("prueba", __name__, url_prefix="/prueba")
auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
me_blueprint = Blueprint("me", __name__, url_prefix="/me")
user_blueprint = Blueprint("user", __name__, url_prefix="/users")
roles_blueprint = Blueprint("roles", __name__, url_prefix="/roles") 

api_blueprint.register_blueprint(prueba_blueprint)
api_blueprint.register_blueprint(auth_blueprint)
api_blueprint.register_blueprint(me_blueprint)
api_blueprint.register_blueprint(user_blueprint)
api_blueprint.register_blueprint(roles_blueprint)


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