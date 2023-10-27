from flask import Blueprint


hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/")


@hello_world_bp.route("/")
def hello_world():
    return "Hello world"
