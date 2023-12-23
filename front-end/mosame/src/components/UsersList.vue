<template>
  <table v-if="users" class="table table-hover">
  <thead class="table-light">
      <tr>
      <th scope="col">Nombre</th>
      <th scope="col">Apellido</th>
      <th scope="col">Email</th>
      <th scope="col">Rol</th>
      <th scope="col">Acciones</th>
      </tr>
  </thead>
  <tbody>
      <tr v-for="user in users" :key="user">
      <td>{{ user.name }}</td>
      <td>{{ user.last_name }}</td>
      <td>{{ user.email }}</td>
      <td>{{ formatRoles(user.roles) }}</td>
      <td>
          <div class="d-flex flex-row column-gap-2">
              <router-link :to="'/usuarios/editar/' + user.id">
                  <button type="button" class="btn btn-outline-primary btn-sm">Editar</button>
              </router-link>
              <button type="button" class="btn btn-outline-danger btn-sm">Eliminar</button>
          </div>
      </td>
      </tr>
  </tbody>
  </table>
  <p v-else>No hay usuarios registrados en el sistema</p>    
</template>

<script>
export default {
  name: "UsersList",
  props: {
    users: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    formatRoles(roles) {
      return roles.map(role => role.name).join(', ');
    },
  },
};
</script>

<style>

</style>