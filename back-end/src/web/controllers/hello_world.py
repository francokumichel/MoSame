from flask import Blueprint, jsonify, render_template
from src.core import prueba


hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/")


@hello_world_bp.route("/")
def hello_world():
    all_pruebas = prueba.list_prueba()
    return render_template("prueba/index.html", pruebas=all_pruebas)
