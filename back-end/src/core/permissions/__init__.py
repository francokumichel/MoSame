from src.core.database import db
from src.core.permissions.role import Role
from src.core.permissions.permission import Permission


def create_permission(**kwargs):
    permission = Permission(**kwargs)
    db.session.add(permission)
    db.session.commit()
    return permission


def create_role(**kwargs):
    role = Role(**kwargs)
    db.session.add(role)
    db.session.commit()
    return role


def list_roles():
    return Role.query.all()

def get_role_by_name(role_name):
    return Role.query.filter_by(name=role_name).first()