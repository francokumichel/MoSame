from flask import Flask
from src.config import config
from src.controllers.hello_world import hello_world_bp


def create_app(env="development", static_folder="../static"):
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    app.register_blueprint(hello_world_bp)

    return app
