<template>
  <!-- Contenedor para la imagen y el selector de rol -->
    <nav v-if="isAuthenticated && user" class="container-xxl px-4 py-4 navbar navbar-expand-lg bg-info bg-opacity-10">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img src="./assets/Logo_MOSaME.png" alt="Logo MOSaME" width="200" height="50">
        </a>
        <div class="d-flex align-items-center column-gap-2">
          <label for="roles" class="text-info fw-bold fs-5">Rol: </label>
          <select class="text-info fw-bold form-select me-2" v-model="selectedRole" @change="getNavigationLinks" aria-label="Default select example">
            <option v-for="rol in user.roles" :key="rol.name" :value="rol.name">{{ rol.name }}</option>
          </select>
        </div>
      </div>
    </nav>

    <!-- Contenedor para los enlaces de navegación -->
    <nav v-if="isAuthenticated && user" class="container-xxl p-4 navbar navbar-expand-lg bg-light shadow-sm">
      <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item" v-for="link in navigationLinks" :key="link.path">
              <router-link class="link-info link-offset-2 link-underline-opacity-0 link-underline-opacity-100-hover fw-bold fs-6 border border-0 me-3" style="--bs-link-hover-color-rgb: 25, 135, 84;" :to="link.path"> {{ link.text }} </router-link>
            </li>
            <li class="nav-item">
              <a class="link-info link-offset-2 link-underline-opacity-0 link-underline-opacity-100-hover fw-bold fs-6 border border-0" style="--bs-link-hover-color-rgb: 25, 135, 84; user-select: none; cursor: pointer;" ref="#" @click="logout">Cerrar sesión</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

  <router-view></router-view>
</template>

<script>
import enlacesPorRol from '@/data/enlaces.js';
import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      navigationLinks: [],
      selectedRole: '',
      roles: [],
    };
  },

  watch: {
    user: {
      immediate: true,
      handler(newValue) {
        if (newValue && newValue.roles && newValue.roles.length > 0) {
          this.selectedRole = newValue.roles[0].name;
          this.getNavigationLinks();
        }
      },
    },
  },

  computed: {
    ...mapGetters(['isAuthenticated', 'user']),
  },

  methods: {
    getNavigationLinks() {
      this.navigationLinks = enlacesPorRol[this.selectedRole] || [];
      this.$store.dispatch("cambiarRol", this.selectedRole);
    },
    logout() {
      this.$store.dispatch("logout");
    },
  },
};
</script>


<style>
.nav-link:hover {
  color: var(--bs-primary);
}
</style>
