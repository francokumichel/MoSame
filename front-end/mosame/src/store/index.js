import { apiService } from "@/services/api";
import { createStore } from "vuex";
import router from "@/router";
import axios from "axios";

export default createStore({
  state: {
    email: null,
    token: null,
    rolActual: null,
    error_msg: "",
  },
  getters: {
    isAuthenticated(state) {
      return state.token !== null;
    },
    userEmail(state) {
      return state.email;
    },
    userRole(state) {
      return state.rolActual;
    },
  },
  mutations: {
    authUser(state, userData) {
      state.email = userData.email;
      state.token = userData.token;
    },
    clearAuthData(state) {
      state.email = null;
      state.token = null;
      state.rolActual = null;
      state.error_msg = "";
    },
    initializeStore(state) {
      if (localStorage.getItem("email")) {
        state.email = `${localStorage.getItem("email")}`;
        state.token = `${localStorage.getItem("token")}`;
      }
    },
    setMsg(state, errorData) {
      state.error_msg = errorData.error_msg;
    },
    setRole(state, selectedRole) {
      state.rolActual = selectedRole;
    }
  },
  actions: {
    login: ({ commit }, authData) => {
      apiService
        .post("/auth", authData)
        .then((response) => {
          let success = response.data.token;

          if (success != null) {
            commit("authUser", {
              email: authData.email,
              token: response.data.token,
            });
            localStorage.setItem("token", response.data.token);
            localStorage.setItem("email", authData.email);
            router.replace("home");
          }
        })
        .catch((error) => {
          commit("setMsg", {
            error_msg: error.response.data.msg,
          });
        });
    },
    logout: ({ commit }) => {
      axios
        .get(import.meta.env.VITE_API_URL + "logout", {
          xsrfCookieName: "csrf_access_token",
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          if (response.status === 200) {
            commit("clearAuthData");
            localStorage.removeItem("email");
            localStorage.removeItem("token");
            router.replace("login");
          }
        })
        .catch((e) => {
          console.log("No se pudo cerrar sesion");
        });
    },
    cambiarRol: ({ commit }, selectedRole) => {
      commit("setRole", selectedRole);
    }
  },
  modules: {},
});
