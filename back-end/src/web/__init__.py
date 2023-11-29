from flask import Flask, redirect, url_for
from src.web.config import config
from src.web.routes import register_routes
from src.core import database
from src.core import seeds
from flask_cors import CORS
from src.web.controllers.hello_world import hello_world_bp

def create_app(env="development", static_folder="../static"):
    app = Flask(__name__, static_folder=static_folder, static_url_path='/public')

    app.config.from_object(config[env])
    database.init_app(app)
    
    #Agregamos CORS
    CORS(app)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    app.register_blueprint(hello_world_bp)
    #register_routes(app)

    @app.get("/")
    def entry_point():
        return redirect(url_for("hello_world.hello_world"))

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seedsdb")
    def seedsdb():
        seeds.run()

    return app
