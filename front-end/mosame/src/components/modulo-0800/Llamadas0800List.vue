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
            <button v-if="llamada.definicion === 'Derivación a CETEC SM'" type="button" class="btn btn-outline-primary btn-sm" data-bs-toggle="modal" data-bs-target="#modalId" @click="verSeguimiento(llamada.id)">Ver seguimiento</button>
        </td>
        </tr>
    </tbody>
    </table>
    <p v-else>No hay llamadas cargadas en el sistema</p>
    <div class="modal fade" id="modalId" tabindex="-1" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-sm" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title fw-bold" id="modalTitleId">Información de Derivación</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>Seguimiento desde CETEC SM: {{ seguimientoDesdeCETECSM }}</p>
            <p v-if="seguimientoDesdeCETECSM != 'No está en seguimiento' && seguimientoDesdeCETECSM != ''">Fecha del último llamado por CETEC SM: {{ fechaUltimoLlamado }}</p>
            <p v-if="seguimientoDesdeCETECSM != 'No está en seguimiento' && seguimientoDesdeCETECSM != ''">Operador de CETEC SM: {{ operadorCETECSM }}</p>
          </div>
        </div>
      </div>
    </div>
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

  data(){
    return {
      seguimientoDesdeCETECSM: '',
      fechaUltimoLlamado: '',
      operadorCETECSM: '',
    }
  },

  methods: {
    
    async verSeguimiento(llamada_id) {
      try {
        this.seguimientoDesdeCETECSM = ''
        const response = await apiService.get(import.meta.env.VITE_API_URL + `0800/verSeguimiento/${llamada_id}`);
        
        if(response.status == 200) {
          if (response.data.esta_asignada) {
            this.seguimientoDesdeCETECSM = 'Está en seguimiento'
            this.fechaUltimoLlamado = `${new Date(response.data.fecha_ult_llamado).getDate() + 1}/${new Date(response.data.fecha_ult_llamado).getMonth() + 1}/${new Date(response.data.fecha_ult_llamado).getFullYear()}`
            this.operadorCETECSM = response.data.operador
          } else {
            this.seguimientoDesdeCETECSM = 'No está en seguimiento'
          }
        }
      } catch(error) {
        displayError(this.$toast, error);
      }
    },
  }, 
};
</script>