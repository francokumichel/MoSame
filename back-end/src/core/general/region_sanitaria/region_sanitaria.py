from src.core.database import db

class RegionSanitaria(db.Model):
    __tablename__ = "region_sanitaria"

    tipo = db.Column(db.String(50), primary_key=True)
    municipios = db.relationship("Municipio", backref="region_sanitaria")
