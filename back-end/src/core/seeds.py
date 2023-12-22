from src.core import prueba
from src.core import users
from src.core import permissions

def run():

    datos_prueba = prueba.create_prueba(
        name="Por favor funciona :)"
    )

    # Permisos acceder a funcionalidades del usuario
    user_index = permissions.create_permission(name="user_index")
    user_new = permissions.create_permission(name="user_new")
    user_destroy = permissions.create_permission(name="user_destroy")
    user_update = permissions.create_permission(name="user_update")
    user_show = permissions.create_permission(name="user_show")
    
    role_admin = permissions.create_role(name="Administrador")

    role_admin.permissions.append(user_index)
    role_admin.permissions.append(user_new)
    role_admin.permissions.append(user_destroy)
    role_admin.permissions.append(user_update)
    role_admin.permissions.append(user_show)

    # Permisos para acceder a permisos a funcionalidades relacionadas a modulo 0800
    call_0800_index = permissions.create_permission(name="call_0800_index")
    call_0800_new = permissions.create_permission(name="call_0800_new")
    call_0800_show = permissions.create_permission(name="call_0800_show")

    role_operator_0800 = permissions.create_role(name="Operador 0800")
    
    role_operator_0800.permissions.append(call_0800_index)
    role_operator_0800.permissions.append(call_0800_new)
    role_operator_0800.permissions.append(call_0800_show)

    # Permisos para acceder a permisos a funcionalidades relacionadas a módulo CETECSM
    # Permisos operador CETECSM
    derivation_index = permissions.create_permission(name="derivation_index")
    derivation_new = permissions.create_permission(name="derivation_new")
    derivation_update = permissions.create_permission(name="derivation_update")
    derivation_show = permissions.create_permission(name="derivation_show")
    call_cetecsm_index = permissions.create_permission(name="call_cetecsm_index")
    call_cetecsm_new = permissions.create_permission(name="call_cetecsm_new")

    # Permisos coordinador CETECSM
    operator_cetecsm_index = permissions.create_permission(name="operator_cetecsm_index")

    role_operator_cetecsm = permissions.create_role(name="Operador CETECSM")
    role_operator_cetecsm.permissions.append(derivation_index)
    role_operator_cetecsm.permissions.append(derivation_new)
    role_operator_cetecsm.permissions.append(derivation_update)
    role_operator_cetecsm.permissions.append(derivation_show)
    role_operator_cetecsm.permissions.append(call_cetecsm_index)
    role_operator_cetecsm.permissions.append(call_cetecsm_new)

    role_coordinator_cetecsm = permissions.create_role(name="Coordinador CETECSM")
    role_coordinator_cetecsm.permissions.append(derivation_index)
    role_coordinator_cetecsm.permissions.append(derivation_show)
    role_coordinator_cetecsm.permissions.append(call_cetecsm_index)
    role_coordinator_cetecsm.permissions.append(call_cetecsm_new)
    role_coordinator_cetecsm.permissions.append(operator_cetecsm_index)

    
    user_admin = users.create_user(
        name="Admin",
        last_name="Admin",
        email="admin@gmail.com",
        password="1234"
    )
    users.update_roles(user_admin, [role_admin])

    user_operator_0800 = users.create_user(
        name="Operador 0800",
        last_name="Operador 0800",
        email="Operador0800@gmail.com",
        password="1234"
    )

    users.update_roles(user_operator_0800, [role_operator_0800])

    user_operator_cetecsm = users.create_user(
        name="Operador CETECSM",
        last_name="Operador CETECSM",
        email="OperadorCETECSM@gmail.com",
        password="1234"
    )

    users.update_roles(user_operator_cetecsm, [role_operator_cetecsm])
    
    user_coordinator_cetecsm = users.create_user(
        name="Coordinador CETECSM",
        last_name="Coordinador CETECSM",
        email="CoordinadorCETECSM@gmail.com",
        password="1234"
    )

    users.update_roles(user_coordinator_cetecsm, [role_coordinator_cetecsm])

    print("Seeds cargados!")

