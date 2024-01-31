<template>
    <table v-if="personasCetecsm" class="table table-hover">
    <thead class="table-light">
        <tr>
        <th scope="col">Fecha de derivacion</th>
        <th scope="col">Presta consentimiento</th>
        <th scope="col">Operador que deriva</th>
        <th scope="col">Región sanitaria</th>
        <th v-if="this.$store.state.rolActual == 'Coordinador CETECSM'" scope="col">Dispositivo que deriva</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Edad</th>
        <th scope="col">DNI</th>
        <th scope="col">Teléfono</th>
        <th scope="col">Teléfono alternativo</th>
        <th scope="col">Municipio</th>
        <th scope="col">Motivo general de la derivación</th>
        <th scope="col">Descripción</th>
        <th v-if="this.$store.state.rolActual == 'Operador CETECSM'" scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="persona in personasCetecsm" :key="persona">
        <td>{{ persona.derivacion.fecha }}</td>
        <td v-if="persona.dio_consentimiento">Si</td>
        <td v-else>No</td>
        <td>{{ persona.derivacion.nombre_operador_derivador }}</td>
        <td>{{ persona.municipio.region_sanitaria.tipo }}</td>
        <td v-if="this.$store.state.rolActual == 'Coordinador CETECSM'" >{{ persona.derivacion.dispositivo_derivacion }}</td>
        <td>{{ persona.nombre }}</td>
        <td>{{ persona.apellido }}</td>
        <td>{{ persona.edad }}</td>
        <td>{{ persona.dni }}</td>
        <td>{{ persona.telefono }}</td>
        <td v-if="persona.telefono_alternativo">{{ persona.telefono_alternativo }}</td>
        <td v-else>-</td>
        <td>{{ persona.municipio.nombre }}</td>
        <td v-if="persona.derivacion.mot_gral_derivacion.tipo != 'Otro'" >{{ persona.derivacion.mot_gral_derivacion.tipo }}</td>
        <td v-else >{{ 'Otro (' + persona.derivacion.mot_gral_derivacion.otro_tipo + ')' }}</td>
        <td>{{ persona.derivacion.descripcion }}</td>
        <td v-if="this.$store.state.rolActual == 'Operador CETECSM'">
            <button type="button" class="btn btn-outline-primary btn-sm" @click="asignarPersona(persona.id)" :disabled="persona.esta_asignada">{{ persona.esta_asignada ? 'Ya asignado' : 'Asignarme' }}</button>
        </td>
        </tr>
    </tbody>
    </table>
    <p v-else>No hay derivaciones registradas en el sistema</p>    
</template>

<script>
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers";

export default {
  name: "PersonasCetecsmList",
  props: {
    personasCetecsm: {
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