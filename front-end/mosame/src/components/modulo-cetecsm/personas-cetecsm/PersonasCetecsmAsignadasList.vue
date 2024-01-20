<template>
    <table v-if="personasAsignadas" class="table table-hover">
    <thead class="table-light">
        <tr>
        <th scope="col">Fecha de próximo llamado</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Edad</th>
        <th scope="col">DNI</th>
        <th scope="col">Teléfono</th>
        <th scope="col">Municipio</th>
        <th scope="col">Región sanitaria</th>
        <th scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="persona in personasAsignadas" :key="persona">
        <td v-if="persona.fecha_prox_llamado_actual">{{ persona.fecha_prox_llamado_actual }}</td>
        <td v-else>-</td>
        <td>{{ persona.nombre }}</td>
        <td>{{ persona.apellido }}</td>
        <td>{{ persona.edad }}</td>
        <td>{{ persona.dni }}</td>
        <td>{{ persona.telefono }}</td>
        <td>{{ persona.municipio.nombre }}</td>
        <td>{{ persona.municipio.region_sanitaria.tipo }}</td>
        <td>
            <div class="d-flex align-items-center column-gap-2">
              <router-link :to="'/cetecsm/persona/perfil/' + persona.id" class="btn btn-outline-primary btn-sm">Ver perfil</router-link>
              <router-link :to="'/cetecsm/llamada/crear/' + persona.id" class="btn btn-outline-success btn-sm">Cargar llamada</router-link>
            </div>
        </td>
        </tr>
    </tbody>
    </table>
    <p v-else>Todavía no posee ninguna persona asignada</p>    
</template>

<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";

export default {
  name: "PersonasCetecsmAsignadasList",
  props: {
    personasAsignadas: {
      type: Array,
      default: () => [],
    },
  },
}
</script>  
