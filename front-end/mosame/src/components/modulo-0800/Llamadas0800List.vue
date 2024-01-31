<template>
    <table v-if="llamadas" class="table table-hover">
    <thead class="table-light">
        <tr>
        <th scope="col">Teléfonos</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">DNI</th>
        <th scope="col">Municipio</th>
        <th scope="col">Edad</th>
        <th scope="col">Definición</th>
        <th scope="col">Detalle</th>
        <th scope="col">Género</th>
        <th scope="col">Pronombre</th>
        <th scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="llamada in llamadas" :key="llamada">
        <td>{{ llamada.telefonos }}</td>
        <td>{{ llamada.nombre }}</td>
        <td>{{ llamada.apellido }}</td>
        <td>{{ llamada.dni }}</td>
        <td>{{ llamada.municipio_nombre }}</td>
        <td>{{ llamada.edad }}</td>
        <td>{{ llamada.definicion }}</td>
        <td>{{ llamada.detalle_intervencion }}</td>
        <td>{{ llamada.identidad_genero_tipo }}</td>
        <td>{{ llamada.pronombre }}</td>
        <td>
            <button v-if="llamada.definicion === 'Derivación a CETEC SM'" type="button" class="btn btn-outline-primary btn-sm">Ver seguimiento</button>
        </td>
        </tr>
    </tbody>
    </table>
    <p v-else>No hay llamadas cargadas en el sistema</p>    
</template>

<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";

export default {
  name: "Llamadas0800List",
  props: {
    llamadas: {
      type: Array,
      default: () => [],
    },
  },

  methods: {
    
    async asignarPersona(personaId) {
      try {
        const response = await apiService.post(import.meta.env.VITE_API_URL + `cetecsm/asignarPersona/${personaId}`);
        
        if(response.status == 200) {
          this.$emit('asignacionRealizada');
          displaySuccess(this.$toast, response.data.msge);
        }
      } catch(error) {
        displayError(this.$toast, error);
      }
    },
  }, 
};
</script>