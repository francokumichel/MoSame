<!-- UsuarioForm.vue -->
<template>
    <div class="border border-secondary-subtle shadow">
      <h2>{{ edit ? 'Editar Usuario' : 'Crear Usuario' }}</h2>
      <form @submit.prevent="saveUser">
        <div class="form-group">
          <label for="nombre">Nombre</label>
          <input v-model="user.name" type="text" id="name" class="form-control" required />
        </div>
  
        <div class="form-group">
          <label for="apellido">Apellido</label>
          <input v-model="user.lastName" type="text" id="lastName" class="form-control" required />
        </div>
  
        <div class="form-group">
          <label for="email">Email</label>
          <input v-model="user.email" type="email" id="email" class="form-control" required />
        </div>
  
        <div class="form-group">
            <label>Roles:</label>
            <div v-for="role in roleOptions()" :key="role.name" class="form-check">
                <input
                    class="form-check-input"
                    type="checkbox"
                    :id="role.name"
                    :value="role.name"
                    :checked="userRoles().includes(role.name)"
                    @change="updateUserRoles(role.name)"
                />
                <label :for="role.name" class="form-check-label">{{ role.name }}</label>
            </div>    
        </div>
        <p>{{ user.roles }}</p>
        <button type="submit" class="btn btn-primary">Guardar</button>
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
                // Si ya está en la lista, quítalo
                this.user.roles = this.user.roles.filter(role => role !== selectedRole);
            } else {
                // Si no está en la lista, agrégalo
                this.user.roles = [...this.user.roles, selectedRole];
            }
        },

    },
    
};
</script>
  
<style>
  
</style>
  