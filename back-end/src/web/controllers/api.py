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

from src.core.users import find_user_by_email, get_user, get_roles
from src.core.schemas.user import user_schema
from src.core.schemas.role import roles_schema

from src.core import prueba
from src.core.schemas.prueba import prueba_schema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
prueba_blueprint = Blueprint("prueba", __name__, url_prefix="/prueba")
auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
me_blueprint = Blueprint("me", __name__, url_prefix="/me") 

api_blueprint.register_blueprint(prueba_blueprint)
api_blueprint.register_blueprint(auth_blueprint)
api_blueprint.register_blueprint(me_blueprint)


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
    roles = get_roles(id=1)
    return make_response(jsonify(roles_schema.dump(roles))), 200