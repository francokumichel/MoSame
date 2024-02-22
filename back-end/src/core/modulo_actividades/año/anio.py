from src.core.database import db
import enum

class Anios(enum.Enum):
    PRIMERO = "1ro"
    SEGUNDO = "2do"
    TERCERO = "3ro"
    CUARTO = "4to"
    QUINTO = "5to"
    SEXTO = "6to"
    SEPTIMO = "7mo"

class Divisiones(enum.Enum):
    PRIMERA = "1ra"
    SEGUNDA = "2da"
    TERCERA = "3ra"
    CUARTA = "4ta"
    QUINTA = "5ta"
    SEXTA = "6ta"
    SEPTIMA = "7ma"
    DIVISION_A = "A"
    DIVISION_B = "B"
    DIVISION_C = "C"
    DIVISION_D = "D"
    DIVISION_E = "E"
    DIVISION_F = "F"
    DIVISION_G = "G"
    DIVISION_H = "H"
    DIVISION_I = "I"
    DIVISION_J = "J"
    DIVISION_K = "K"
    DIVISION_L = "L"

class Anio(db.Model):
    __tablename__ = "anio"

    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String(5))
    divisiones = db.Column(db.Text)

