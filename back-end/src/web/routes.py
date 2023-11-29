from src.web.controllers.hello_world import hello_world_bp


def register_routes(app):
    app.register_blueprint(hello_world_bp)
