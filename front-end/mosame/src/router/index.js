import { createRouter, createWebHistory } from 'vue-router'
import LoginView from "../views/LoginView.vue";
import UsersView from"../views/UsersView.vue";
import FormUsers from "../views/FormUserView.vue";
import PersonasCetecsm from "../views/PersonaCetecsmView.vue";
import CreateDerivacionView from "../views/CreateDerivacionView.vue";
import PersonasCetecsmAsignadas from "../views/PersonasCetecsmAsignadasView.vue";
import PerfilPersonaCetecsm from "../views/PerfilPersonaCetecsmView.vue";
import PersonaCetecsmLlamadas from "../views/PersonaCetecsmLlamadasView.vue";
import EditarPersonaCetecsmAsignada from "../views/EditarPersonaCetecsmAsignadaView.vue";
import CreateLlamadaCetecsm from "../views/CreateLlamadaCetecsmView.vue";
import OperadoresCetecsm from "../views/modulo-cetecsm/OperadoresCetecsmView.vue";
import PersonasAsignadasTodasCetecsm from "../views/modulo-cetecsm/PersonasAsignadasTodasCetecsmView.vue"
import store from "@/store";


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
            meta: { requiresAuth: true },
        },
        {
            path:"/users/create",
            name: "users-create",
            component: FormUsers,
            meta: { requiresAuth: true },
        },
        {
            path:"/users/update/:id",
            name: "users-update",
            component: FormUsers,
            meta: { requiresAuth: true },
        },
        {
            path:"/cetecsm/derivaciones",
            name: "cetecsm-derivaciones",
            component: PersonasCetecsm,
            meta: { requiresAuth: true }, 
        },
        {
            path:"/cetecsm/derivacion/create",
            name: "cetecsm-derivacion-create",
            component: CreateDerivacionView,
            meta: { requiresAuth: true },
        },
        {
            path:"/cetecsm/asignaciones/:id(\\d+)?",
            name: "cetecsm-asignaciones",
            component: PersonasCetecsmAsignadas,
            meta: { requiresAuth: true },             
        },
        {
            path:"/cetecsm/persona/perfil/:id",
            name: "cetecsm-perfil-persona",
            component: PerfilPersonaCetecsm,
            meta: { requiresAuth: true },             
        },
        {
            path:"/cetecsm/persona/llamadas/:id",
            name: "cetecsm-persona-llamadas",
            component: PersonaCetecsmLlamadas,
            meta: { requiresAuth: true },             
        },
        {
            path:"/cetecsm/persona/editar/:id",
            name: "cetecsm-editar-persona",
            component: EditarPersonaCetecsmAsignada,
            meta: { requiresAuth: true },             
        },
        {
            path:"/cetecsm/llamada/crear/:id",
            name: "cetecsm-crear-llamada",
            component: CreateLlamadaCetecsm,
            meta: { requiresAuth: true },             
        },
        {
            path:"/cetecsm/operadores",
            name: "cetecsm-operadores",
            component: OperadoresCetecsm,
            meta: { requiresAuth: true },             
        },
        {
            path:"/cetecsm/personas/asignadas_todas",
            name: "cetecsm-personas-asignadas-todas",
            component: PersonasAsignadasTodasCetecsm,
            meta: { requiresAuth: true },             
        },
    ],
});

router.beforeEach((to, from, next) => {
    if (to.matched.some((route) => route.meta.requiresAuth)) {
        if (!store.state.email) {
            next("/login");
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router

  