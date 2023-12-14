from src.core import prueba
from src.core import users
from src.core import permissions

def run():

    datos_prueba = prueba.create_prueba(
        name="Por favor funciona :)"
    )

    user_index = permissions.create_permission(name="user_index")
    user_new = permissions.create_permission(name="user_new")
    user_destroy = permissions.create_permission(name="user_destroy")
    user_update = permissions.create_permission(name="user_update")
    user_show = permissions.create_permission(name="user_show")
    
    role_admin = permissions.create_role(name="admin")

    role_admin.permissions.append(user_index)
    role_admin.permissions.append(user_new)
    role_admin.permissions.append(user_destroy)
    role_admin.permissions.append(user_update)
    role_admin.permissions.append(user_show)
    
    user_admin = users.create_user(
        name="Admin",
        last_name="Admin",
        email="admin@gmail.com",
        password="1234"
    )
    users.update_roles(user_admin, [role_admin])


    print("Seeds cargados!")

