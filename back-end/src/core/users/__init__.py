from src.core.users.user import User
from src.core.persona_cetecsm.persona_cetecsm import PersonaCetecsm
from src.core.permissions.role import Role
from src.core.permissions import get_role_by_name
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
#        rol = get_role_by_name(role_name=role_name)
        user.roles.append(rol)
    db.session.add(user)
    db.session.commit()
    return user

def update_roles(user, rolesSelected):
    user.roles = []
    db.session.commit()
    assigned_roles(user, rolesSelected)
    return user

def list_users(page_num, per_page):
    """ Consulta a la bd y obtiene todos los registros paginados de los usuarios registrados en el sistema """

    return User.query.order_by(User.id).paginate(page=page_num, per_page=per_page, error_out=True)

def asignar_persona(user, persona):
    user.personas_cetecsm_asignadas.append(persona)
    db.session.commit()
    return user

def get_personas_asignadas(search_term, page_num, per_page, user_id):
    user = get_user(id=user_id)
    personas_asignadas = PersonaCetecsm.query.join(User, User.id == PersonaCetecsm.usuario_id).filter(User.id == user_id)
    
    if search_term:
        personas_asignadas = personas_asignadas.filter(
            (PersonaCetecsm.nombre.ilike(f"%{search_term}%")) |
            (PersonaCetecsm.apellido.ilike(f"%{search_term}%"))
        )

    personas_asignadas = personas_asignadas.order_by(PersonaCetecsm.id)

    return personas_asignadas.paginate(page=page_num, per_page=per_page, error_out=True)

#    return personas_asignadas.order_by(PersonaCetecsm.id).paginate(page=page_num, per_page=per_page, error_out=True)    