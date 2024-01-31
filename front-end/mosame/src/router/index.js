import { createRouter, createWebHistory } from 'vue-router'
import LoginView from "../views/LoginView.vue";
import UsersView from"../views/UsersView.vue";
import FormUsers from "../views/FormUserView.vue";
import HomeView from "../views/HomeView.vue";
import PersonasCetecsm from "../views/PersonaCetecsmView.vue";
import CreateDerivacionView from "../views/CreateDerivacionView.vue";
import PersonasCetecsmAsignadas from "../views/PersonasCetecsmAsignadasView.vue";
import PerfilPersonaCetecsm from "../views/PerfilPersonaCetecsmView.vue";
import PersonaCetecsmLlamadas from "../views/PersonaCetecsmLlamadasView.vue";
import EditarPersonaCetecsmAsignada from "../views/EditarPersonaCetecsmAsignadaView.vue";
import CreateLlamadaCetecsm from "../views/CreateLlamadaCetecsmView.vue";
import OperadoresCetecsm from "../views/modulo-cetecsm/OperadoresCetecsmView.vue";
import PersonasAsignadasTodasCetecsm from "../views/modulo-cetecsm/PersonasAsignadasTodasCetecsmView.vue"
import PersonasCetecsmDerivadas from "../views/modulo-observatorio/PersonasCetecsmDerivadasView.vue";
import PersonasCetecsmSeguimiento from "../views/modulo-observatorio/PersonasCetecsmSeguimientoView.vue";
import CantidadLlamadasCetecsm from "../views/modulo-observatorio/CantidadLlamadasCetecsmView.vue";
import CreateLlamadaCetecsm from "../views/CreateLlamadaCetecsmView.vue";
import CreateLlamada0800View from "../views/CreateLlamada0800View.vue";
import Llamadas0800View from "../views/Llamadas0800View.vue";
import store from "@/store";
import { displayError } from "@/services/handlers.js"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/login",
            name: "login",
            component: LoginView,
        },
        {
            path: "/users",
            name: "users",
            component: UsersView,
            meta: { requiresAuth: true, roles: ["Administrador"] },
        },
        {
            path: "/home",
            name: "home",
            component: HomeView,
            meta: { requiresAuth: true },
        },
        {
            path:"/users/create",
            name: "users-create",
            component: FormUsers,
            meta: { requiresAuth: true, roles: ["Administrador"] },
        },
        {
            path:"/users/update/:id",
            name: "users-update",
            component: FormUsers,
            meta: { requiresAuth: true, roles: ["Administrador"] },
        },
        {
            path:"/cetecsm/derivaciones",
            name: "cetecsm-derivaciones",
            component: PersonasCetecsm,
            meta: { requiresAuth: true, roles: ["Operador CETECSM"] }, 
        },
        {
            path:"/cetecsm/derivacion/create",
            name: "cetecsm-derivacion-create",
            component: CreateDerivacionView,
            meta: { requiresAuth: true, roles: ["Operador CETECSM"] },
        },
        {
            path:"/cetecsm/asignaciones/:id(\\d+)?",
            name: "cetecsm-asignaciones",
            component: PersonasCetecsmAsignadas,
            meta: { requiresAuth: true, roles: ["Operador CETECSM", "Coordinador CETECSM"] },             
        },
        {
            path:"/cetecsm/persona/perfil/:id",
            name: "cetecsm-perfil-persona",
            component: PerfilPersonaCetecsm,
            meta: { requiresAuth: true, roles: ["Operador CETECSM", "Coordinador CETECSM"] },             
        },
        {
            path:"/cetecsm/persona/llamadas/:id",
            name: "cetecsm-persona-llamadas",
            component: PersonaCetecsmLlamadas,
            meta: { requiresAuth: true, roles: ["Operador CETECSM", "Coordinador CETECSM"] },             
        },
        {
            path:"/cetecsm/persona/editar/:id",
            name: "cetecsm-editar-persona",
            component: EditarPersonaCetecsmAsignada,
            meta: { requiresAuth: true, roles: ["Operador CETECSM"] },             
        },
        {
            path:"/cetecsm/llamada/crear/:id",
            name: "cetecsm-crear-llamada",
            component: CreateLlamadaCetecsm,
            meta: { requiresAuth: true, roles: ["Operador CETECSM", "Coordinador CETECSM"] },
        },
        {
            path:"/modulo_0800/cargar_llamada",
            name: "0800-crear-llamada",
            component: CreateLlamada0800View,
            meta: { requiresAuth: true },
        },
        {
            path:"/modulo_0800/llamadas",
            name: "0800-llamadas",
            component: Llamadas0800View,
            meta: { requiresAuth: true },
        },
        {
            path:"/cetecsm/operadores",
            name: "cetecsm-operadores",
            component: OperadoresCetecsm,
            meta: { requiresAuth: true, roles: ["Coordinador CETECSM"] },             
        },
        {
            path:"/cetecsm/personas/asignadas_todas",
            name: "cetecsm-personas-asignadas-todas",
            component: PersonasAsignadasTodasCetecsm,
            meta: { requiresAuth: true, roles: ["Coordinador CETECSM"] },             
        },
        {
            path:"/observatorio/personas_cetecsm_derivadas",
            name: "observatorio-personas-cetecsm-derivadas",
            component: PersonasCetecsmDerivadas,
            meta: { requiresAuth: true, roles: ["Miembro observatorio"] },             
        },
        {
            path:"/observatorio/personas_cetecsm_seguimiento",
            name: "observatorio-personas-cetecsm-seguimiento",
            component: PersonasCetecsmSeguimiento,
            meta: { requiresAuth: true, roles: ["Miembro observatorio"] },             
        },
        {
            path:"/observatorio/cantidad_llamadas_cetecsm",
            name: "observatorio-cantidad-llamadas-cetecsm",
            component: CantidadLlamadasCetecsm,
            meta: { requiresAuth: true, roles: ["Miembro observatorio"] },             
        },
    ],
});

function hasPermission(route, userRoles) {
    if (!route.meta.roles || route.meta.roles.length === 0) {
        // La ruta no tiene restricciones de roles, por lo que se permite el acceso
        return true;
    }

    return route.meta.roles.some((role) => userRoles.includes(role));
}

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some((route) => route.meta.requiresAuth);

    if (requiresAuth) {
        // Verificar la autenticación
        if (!store.getters.isAuthenticated) {
            next("/login");
            return;
        }

        // Verificar los roles
        const userRoles = store.getters.userRole;
        if (!hasPermission(to, userRoles)) {
            // El usuario no tiene permisos para acceder a la ruta
            displayError(toast, "No estas autorizado a acceder a esta ruta");
            next("/login");
            return;
        }
    }

    next();
});


export default router

  