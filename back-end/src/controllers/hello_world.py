from flask import Blueprint, jsonify


hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/")


@hello_world_bp.route("/")
def hello_world():
    return jsonify({"hola": "hola", "mundo": "mundo"}, 200)
