<!-- UsuarioForm.vue -->
<template>
    <div class="p-4 border border-secondary-subtle shadow">
      <h2 class="fw-bold mb-4">{{ edit ? 'Editar Usuario' : 'Crear Usuario' }}</h2>
      <form @submit.prevent="saveUser">
        <div class="row mb-3">
          <label for="nombre" class="col-sm-2 col-form-label fw-semibold">Nombre</label>
          <div class="col-sm-7">
            <input maxlength="50" v-model="user.name" type="text" id="name" class="form-control shadow-sm" required />
          </div>
        </div>
  
        <div class="row mb-3">
          <label for="apellido" class="col-sm-2 col-form-label fw-semibold">Apellido</label>
          <div class="col-sm-7">
            <input maxlength="50" v-model="user.lastName" type="text" id="lastName" class="form-control shadow-sm" required />
          </div>
        </div>
  
        <div class="row mb-3">
          <label for="email" class="col-sm-2 col-form-label fw-semibold">Email</label>
          <div class="col-sm-7">
            <input maxlength="50" v-model="user.email" type="email" id="email" class="form-control shadow-sm" required />
          </div>
        </div>
        
        <fieldset class="row mb-3">
            <legend class="col-form-label col-sm-2 pt-0 fw-semibold">Roles</legend>
            <div class="col-sm-10">
                <div v-for="role in roleOptions()" :key="role.name" class="form-check">
                    <input
                        class="form-check-input shadow-sm"
                        type="checkbox"
                        :id="role.name"
                        :value="role.name"
                        :checked="userRoles().includes(role.name)"
                        @change="updateUserRoles(role.name)"
                    />
                    <label :for="role.name" class="form-check-label">{{ role.name }}</label>
                </div>
            </div>    
        </fieldset>
        <div class="d-flex justify-content-center">
            <button type="submit" class="btn btn-info text-white fw-semibold shadow-sm">Guardar</button>
        </div>    
      </form>
    </div>
  </template>
  
<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";


export default {
    data() {
        return {
            edit: false,
            roles: [],
            user: { name: '', lastName: '', email: '', roles: [] },
            errors: [],
        };
    },
    async created() {
        await apiService.get(import.meta.env.VITE_API_URL + "roles/index")
            .then((response) => {
                this.roles = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })

        this.edit = !!this.$route.params.id;
        if (this.edit) {
            try {
                const response = await apiService.get(import.meta.env.VITE_API_URL + "users/show/" + this.$route.params.id);
                this.user = response.data;
            } catch (error) {
                this.errors.push(error);
            }
        }
    },
    methods: {
        async saveUser() {
            if (this.edit) {
                try {
                    await apiService.post(import.meta.env.VITE_API_URL + "users/update/" + this.$route.params.id,
                    {
                        name: this.user.name,
                        lastName: this.user.lastName,
                        email: this.user.email,
                        roles: this.user.roles,
                    })
                    .then((response) => {
                        if(response.status == 200) {
                            displaySuccess(this.$toast, "Usuario actualizado exitosamente.");
                            this.$router.push("/users");
                        }
                    })
                } catch(error) {
                    displayError(this.$toast, error);
                    this.errors.push(error);
                }
            } else {
                try {
                    await apiService.post(import.meta.env.VITE_API_URL + "users/create", 
                    {
                        name: this.user.name,
                        lastName: this.user.lastName,
                        email: this.user.email,
                        roles: this.user.roles,
                    })
                    .then((response) => {
                        if(response.status == 200) {
                            displaySuccess(this.$toast, "Usuario registrado exitosamente");
                            this.$router.push("/users");
                        }
                    })
                } catch(error) {
                    displayError(this.$toast, error);
                    this.errors.push(error);
                }
            }
        },
        
        roleOptions() {
            return this.roles.map(role => ({ name: role.name }));
        },

        userRoles() {
            return this.user.roles.map(role => role.name);
        },

        updateUserRoles(selectedRole) {
            console.log(selectedRole)
            if (this.user.roles.includes(selectedRole)) {
                this.user.roles = this.user.roles.filter(role => role !== selectedRole);
            } else {
                this.user.roles = [...this.user.roles, selectedRole];
            }
        },

    },
    
};
</script>
  
<style>
  
</style>
  