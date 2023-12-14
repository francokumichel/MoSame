import os
import urllib
from dotenv import load_dotenv


class Config(object):
    """Base configuration."""

    SECRET_KEY = "secret"
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = "super-secret"
    JWT_TOKEN_LOCATION = "headers"
    PROPAGATE_EXCEPTIONS = True
    CORS_SUPPORTS_CREDENTIALS = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    load_dotenv()

    # Para Flask-Session
    SESSION_TYPE = "filesystem"


class ProductionConfig(Config):
    """Production configuration."""

    pass


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    string_connection = connection_string = f"DRIVER={os.getenv('DB_DRIVER')};Database={os.getenv('DB_DATABASE')};SERVER={os.getenv('DB_SERVER')};UID={os.getenv('DB_UID')};PWD={os.getenv('DB_PWD')}"
    string_connection = urllib.parse.quote_plus(string_connection)
    string_connection = "mssql+pyodbc:///?odbc_connect=%s" % string_connection
    SQLALCHEMY_DATABASE_URI = string_connection
    SQLALCHEMY_TRACK_MODIFICATIONS=True


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True


config = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig,
}
