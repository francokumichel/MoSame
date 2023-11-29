from flask import (
    Blueprint,
    jsonify,
    make_response,
    request,
)

from src.core import prueba
from src.core.schemas.prueba import PruebaSchema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/")
prueba_blueprint = Blueprint("prueba", __name__, url_prefix="/prueba")

api_blueprint.register_blueprint(prueba_blueprint)

def JSON_serialized_response(records, schema):
    resp = make_response(jsonify(schema.dump(records)))
    resp.headers["Content-Type: application/json"] = "*"
    return resp

@prueba_blueprint.get("/pruebas")  # La url seria /api/club/disciplines
def get_all_pruebas():
    records = prueba.list_disciplines_plain()
    schema = PruebaSchema(many=True)
    return JSON_serialized_response(records, schema)



