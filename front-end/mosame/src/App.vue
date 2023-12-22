<template>
  <div v-if="$store.state.token">
    <nav class="container-xxl py-3 navbar navbar-expand-lg bg-info text-white">
      <div class="container-fluid">
        <a class="navbar-brand text-white fs-3" href="#">Mosame</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item" v-for="link in navigationLinks" :key="link.path">
              <router-link class="nav-link text-white" :to="link.path"> {{ link.text }} </router-link>
            </li>
          </ul>
          <div class="d-flex align-items-center column-gap-2">
            <label for="roles">Rol: </label>
            <select class="form-select me-2" v-model="selectedRole" @change="getNavigationLinks" aria-label="Default select example">
              <option v-for="rol in roles" :key="rol.name" :value="rol.name">{{ rol.name }}</option>
            </select>
          </div>
        </div>
      </div>
    </nav>
  </div>
  <router-view></router-view>
</template>

<script>
import enlacesPorRol from '@/data/enlaces.js';
import axios from "axios";

export default {
  data() {
    return {
      navigationLinks: [],
      selectedRole: '',
      roles: [],
    };
  },

  async created() {
    axios
      .get(import.meta.env.VITE_API_URL + "me/roles", {
        xsrfCookieName: "csrf_access_token",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.roles = response.data;
        if (this.roles.length > 0) {
          this.selectedRole = this.roles[0].name;
        this.getNavigationLinks()  
    }
      })
      .catch((e) => {
        console.log(e)
        this.errores.push(e);
      });
  },

  methods: {
    getNavigationLinks() {
      this.navigationLinks = enlacesPorRol[this.selectedRole] || [];
      console.log(this.navigationLinks)
    },
  },
};
</script>


<style>

</style>
