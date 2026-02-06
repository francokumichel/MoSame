import os
import urllib
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base configuration."""
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret")
    JWT_TOKEN_LOCATION = "headers"
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"
    JWT_COOKIE_CSRF_PROTECT = False
    PROPAGATE_EXCEPTIONS = True
    CORS_SUPPORTS_CREDENTIALS = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    SESSION_TYPE = "filesystem"

class ProductionConfig(Config):
    """Production configuration."""
    pass

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    
    # Guardamos los valores individuales para que reset_db los use con pyodbc
    DB_DRIVER = os.getenv('DB_DRIVER', '{ODBC Driver 17 for SQL Server}')
    DB_SERVER = os.getenv('DB_SERVER', 'db') # 'db' es el nombre del servicio en docker-compose
    DB_DATABASE = os.getenv('DB_DATABASE', 'MoSameDB')
    DB_UID = os.getenv('DB_UID', 'sa')
    DB_PWD = os.getenv('DB_PWD', 'MoSame_Password_123')

    # Construcción de la URI para SQLAlchemy
    raw_connection = (
        f"DRIVER={DB_DRIVER};"
        f"SERVER={DB_SERVER};"
        f"Database={DB_DATABASE};"
        f"UID={DB_UID};"
        f"PWD={DB_PWD};"
        "TrustServerCertificate=yes;"
    )
    params = urllib.parse.quote_plus(raw_connection)
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True

config = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig,
}