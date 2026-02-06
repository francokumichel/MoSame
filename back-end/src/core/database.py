import pyodbc
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    config_db(app)

def config_db(app):
    " Configuracion de la aplicacion "
    @app.teardown_request
    def close_session(exception=None):
        db.session.close()

def reset_db():

    driver = current_app.config.get('DB_DRIVER')
    server = current_app.config.get('DB_SERVER')
    database = current_app.config.get('DB_DATABASE')
    uid = current_app.config.get('DB_UID')
    pwd = current_app.config.get('DB_PWD')

    try:
        print(f"Verificando existencia de la base de datos '{database}' en {server}...")
        conn_str = f'DRIVER={driver};SERVER={server};DATABASE=master;UID={uid};PWD={pwd};TrustServerCertificate=yes'
        
        conn = pyodbc.connect(conn_str, autocommit=True)
        cursor = conn.cursor()
        
        cursor.execute(f"IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{database}') CREATE DATABASE [{database}]")
        cursor.close()
        conn.close()
        print("Base de datos verificada/creada.")
        
    except Exception as e:
        print(f"Error al intentar crear la base de datos: {e}")

    print("Eliminando tablas existentes (drop_all)...")
    db.drop_all()
    print("Creando nuevas tablas (create_all)...")
    db.create_all()
    print("Base de datos reseteada y esquemas creados con éxito.")