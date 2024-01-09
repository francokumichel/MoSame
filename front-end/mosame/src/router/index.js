import { createRouter, createWebHistory } from 'vue-router'
import LoginView from "../views/LoginView.vue";
import UsersView from"../views/UsersView.vue";
import FormUsers from "../views/FormUserView.vue";
import PersonasCetecsm from "../views/PersonaCetecsmView.vue";
import CreateDerivacionView from "../views/CreateDerivacionView.vue";
import PersonasCetecsmAsignadas from "../views/PersonasCetecsmAsignadasView.vue"
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
            path:"/cetecsm/asignaciones",
            name: "cetecsm-asignaciones",
            component: PersonasCetecsmAsignadas,
            meta: { requiresAuth: true },             
        }
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

  