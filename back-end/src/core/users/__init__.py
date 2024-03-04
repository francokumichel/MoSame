from src.core.users.user import User, users_roles
from src.core.persona_cetecsm.persona_cetecsm import PersonaCetecsm
from src.core.llamada_cetecsm.llamada_cetecsm import LlamadaCetecsm
from src.core.permissions.role import Role
from src.core.permissions import get_role_by_name
from src.core.database import db
from sqlalchemy import func, distinct, and_
from datetime import datetime

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
        rol = get_role_by_name(role_name=rol)
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
    persona.esta_asignada = True
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

def get_operadores_cetecsm(page, per_page):
    subquery = (
        db.session.query(PersonaCetecsm.usuario_id, func.max(LlamadaCetecsm.fecha_llamado).label('fecha_ultimo_llamado'))
        .join(LlamadaCetecsm, PersonaCetecsm.id == LlamadaCetecsm.persona_cetecsm_id)
        .group_by(PersonaCetecsm.usuario_id)
        .subquery()
    )

    asignaciones = (
        db.session.query(
            User.id,
            User.email,
            User.name,
            User.last_name,
            func.count(distinct(PersonaCetecsm.id)).label('cantidad_personas_asignadas'),
            func.format(subquery.c.fecha_ultimo_llamado, 'yyyy-MM-dd').label('fecha_ultimo_llamado')
        )
        .outerjoin(subquery, User.id == subquery.c.usuario_id)
        .outerjoin(PersonaCetecsm, (User.id == PersonaCetecsm.usuario_id) & (PersonaCetecsm.esta_activa == True))
        .outerjoin(users_roles, User.id == users_roles.c.user_id)
        .outerjoin(Role, users_roles.c.role_id == Role.id)
        .filter(Role.name == 'Operador CETECSM')  # Condición para el rol específico
        .group_by(User.id, User.email, User.name, User.last_name, subquery.c.fecha_ultimo_llamado)
        .order_by(User.id)
    )

    return asignaciones.paginate(page=page, per_page=per_page, error_out=True)

def obtener_total_llamados_cetecsm(fecha_desde=None, fecha_hasta=None, usuario_id=None, resolucion=None):
    filtros = []

    if fecha_desde:
        filtros.append(LlamadaCetecsm.fecha_llamado >= fecha_desde)

    if fecha_hasta:
        filtros.append(LlamadaCetecsm.fecha_llamado <= fecha_hasta)

    if usuario_id:
        filtros.append(LlamadaCetecsm.usuario_id == usuario_id)

    if resolucion:
        filtros.append(LlamadaCetecsm.resolucion == resolucion)

    filtro_final = and_(*filtros)

    total_llamados = db.session.query(func.count(LlamadaCetecsm.id)).filter(filtro_final).scalar()

    return total_llamados

def obtener_usuario_por_rol(rol):
    usuarios_operadores = User.query.filter(User.roles.any(Role.name == rol)).all()

    return usuarios_operadores