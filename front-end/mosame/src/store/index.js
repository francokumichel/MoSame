import { apiService } from "@/services/api";
import { createStore } from "vuex";
import router from "@/router";
import axios from "axios";

export default createStore({
  state: {
    email: null,
    token: null,
    error_msg: "",
  },
  getters: {
    isAuthenticated(state) {
      return state.token !== null;
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
      apiService
        .get(import.meta.env.VITE_API_URL + "logout")
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
  },
  modules: {},
});
