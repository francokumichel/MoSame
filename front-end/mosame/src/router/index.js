import { createRouter, createWebHistory } from 'vue-router'
import LoginView from "../views/LoginView.vue";
import UsersView from"../views/UsersView.vue";
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
            path: "/usuarios",
            name: "usuarios",
            component: UsersView,
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

  