import { apiService } from "@/services/api";
import { createStore } from "vuex";
import router from "@/router";
import axios from "axios";

export default createStore({
  state: {
    user: JSON.parse(localStorage.getItem('user')) || {},
    token: null,
    rolActual: null,
    error_msg: "",
  },
  getters: {
    isAuthenticated(state) {
      return state.token !== null;
    },
    user(state) {
      return state.user;
    },
    userRole(state) {
      return state.rolActual;
    },
  },
  mutations: {
    setUser(state, user){
      state.user = user;
    },

    setToken(state, token){
      state.token = token;
    },

    clearAuthData(state) {
      state.email = null;
      state.token = null;
      state.rolActual = null;
      state.error_msg = "";
    },
    initializeStore(state) {
      const storedUser = JSON.parse(localStorage.getItem('user'))
      const storedToken = localStorage.getItem('token')
    
      if (storedUser && storedToken) {
        state.user = storedUser
        state.token = storedToken
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
    login: ({ commit, dispatch }, authData) => {
      apiService
        .post("/auth", authData)
        .then((response) => {
          let success = response.data.token;
          if (success != null) {
            commit("setToken", response.data.token);
            localStorage.setItem("token", response.data.token);
            dispatch("fetchUser");
          }
        })
        .catch((error) => {
          commit("setMsg", {
            error_msg: error.response.data.msg,
          });
        });
    },

    fetchUser: ({ commit }) => {
      axios
        .get(import.meta.env.VITE_API_URL + "me/profile", {
          xsrfCookieName: "csrf_access_token",
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          if(response.status == 200) {
            console.log(response)
            commit("setUser", response.data);
            localStorage.setItem("user", JSON.stringify(response.data));
            router.push("/");
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
            localStorage.removeItem("user");
            localStorage.removeItem("token");
            router.push("/login")
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
