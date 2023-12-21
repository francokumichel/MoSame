from src.core.users.user import User
from src.core.permissions.role import Role
from src.core.database import db

def create_user(**kwargs):
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user


def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user


def get_user(id):
    user = User.query.get(id)
    return user

def get_roles(id):
    user = get_user(id)
    return user.roles


def update_user(**kwargs):
    user = get_user(kwargs["id"])
    user.update(**kwargs)
    db.session.commit()
    return user


def find_user_by_email(email):
    return User.query.filter_by(email=email).first()


def assigned_roles(user, rolesSelected):
    """Agrega uno o más roles a un usuario

    Args:
        user (User): Usuario del cual se actualizarán sus roles
        rolesSelected (List[]): Lista de roles a agregar
    """

    for rol in rolesSelected:
        user.roles.append(rol)
    db.session.add(user)
    db.session.commit()
    return user

def update_roles(user, rolesSelected):
    user.roles = []
    db.session.commit()
    assigned_roles(user, rolesSelected)
    return user