from src.core.database import db
from src.core.general.region_sanitaria.region_sanitaria import RegionSanitaria

def create_region_sanitaria(**kwargs):
    region_sanitaria = RegionSanitaria(**kwargs)
    db.session.add(region_sanitaria)
    db.session.commit()
    return region_sanitaria

def list_regiones_sanitarias():
    return RegionSanitaria.query.all()

def get_by_tipo(tipo):
    return RegionSanitaria.query.filter_by(tipo=tipo).first()
