from flask import (
    Blueprint,
    jsonify,
    make_response,
    request,
)

from src.core import prueba
from src.core.schemas.prueba import prueba_schema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
prueba_blueprint = Blueprint("prueba", __name__, url_prefix="/prueba")

api_blueprint.register_blueprint(prueba_blueprint)

@prueba_blueprint.get("")
def get_all_pruebas():
    records = prueba.list_prueba()
    return jsonify(prueba_schema.dump(records))



