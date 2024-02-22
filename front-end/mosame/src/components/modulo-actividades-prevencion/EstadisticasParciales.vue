<template>
  <div class="shadow-sm p-3">
    <h4 class="fw-semibold mb-3">Estadística {{ tipoEstadistica }}</h4>
    <div class="row g-3 mb-4">
      <div class="col-auto ms-3">
        <label for="tipos_actividad" class="mb-1">Tipo taller: </label>
        <select class="form-select" v-model="tipoTaller" @change="cargarActividades" aria-label="Default select example">
            <option v-for="tipo in tiposTaller" :key="tipo" :value="tipo">{{ tipo }}</option>
        </select>
      </div>
      <div class="col-auto">
        <label for="tipos_actividad" class="mb-1">Tipo estadística: </label>
        <select class="form-select" v-model="tipoEstadistica" aria-label="Default select example">
            <option value="Parcial">Parcial</option>
            <option value="Total">Total</option>
        </select>            
      </div>
      <div v-if="tipoEstadistica == 'Parcial'" class="col-auto">
        <label for="tipos_actividad" class="mb-1">Agrupar por: </label>
        <select class="form-select" v-model="paramAgrupacion" @change="updatePerPage" aria-label="Default select example">
            <option value="Región sanitaria">Región sanitaria</option>
            <option value="Dispositivo">Dispositivo</option>
            <option value="Municipio">Municipio</option>
        </select>
      </div>
      <div v-if="tipoTaller != 'Talleres de Salud Mental en las Escuelas'" class="col-auto">
        <label for="tipos_actividad" class="mb-1">Actividad: </label>
        <select class="form-select" v-model="tipoActividad" @change="updatePerPage" aria-label="Default select example">
            <option>Todas</option>
            <option v-for="actividad in actividades" :key="actividad" :value="actividad.nombre">{{ actividad.nombre }}</option>
        </select>
      </div>
    </div>
    <EstadisticasTabla :estadisticas="estadisticas" :tipoTaller="tipoTaller" :paramAgrupacion="paramAgrupacion"/>
    <div class="d-flex flex-row justify-content-center align-items-center">
      <div class="d-flex flex-row ms-auto align-items-center me-3">
        <div class="d-flex flex-row align-items-center mb-3 me-2 column-gap-3">
          <label>Filas por página: </label>
          <input class="form-control-sm bg-light" type="number" name="per_page" id="per_page"
          min="1" v-model="perPage" :max="cantPages" @input="updatePerPage" />
          <p class="mb-0">{{ pageInfo }}</p>
        </div>
        <nav class="ms-5 me-2" aria-label="Page navigation example">
          <ul class="pagination">
            <li @click="previousPage" :class="{ 'disabled': page === 1 }" class="page-item">
              <a class="page-link border border-0" href="#" aria-label="Previous">
                  <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li @click="nextPage" :class="{ 'disabled': page*this.perPage >= this.cantPages }" class="page-item">
              <a class="page-link border border-0" href="#" aria-label="Next">
                  <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
import EstadisticasTabla from './EstadisticasTabla.vue';
import { apiService } from "@/services/api";

export default {
  data() {
    return {
      estadisticas: [],
      errores: [],
      paramAgrupacion: 'Municipio',
      tipoActividad: 'Todas',
      tiposTaller: [],
      tipoTaller: '',
      actividades: [],
      tipoEstadistica: 'Parcial',
      page: 1,
      perPage: 5,
      cantPages: 0,
    }
  },

  async created() {
    await apiService.get(import.meta.env.VITE_API_URL + "actividades/tipos_taller")
      .then((response) => {
          this.tiposTaller = response.data;
          this.tipoTaller = this.tiposTaller.TALLERES;
      })
      .catch((e) => {
          console.log(e)
          this.errores.push(e);
      })  
    this.cargarEstadisticas();
  },

  components: { EstadisticasTabla },

  computed: {
    pageInfo() {
        const start = (this.page - 1) * this.perPage + 1;
        const end = Math.min(start + this.perPage - 1, this.cantPages);
        return `${start}-${end} de ${this.cantPages}`;
    }
  },

  watch: {
    tipoTaller(newTipoTaller) {
      if(this.tipoTaller != this.tiposTaller.TALLERES) {
        this.tipoActividad = 'Todas';
        this.cargarActividades();
      }
      this.updatePerPage();
    },
    tipoEstadistica(newTipoEstadistica) {
      this.tipoEstadistica == 'Total' ? this.paramAgrupacion = 'Año' : this.paramAgrupacion = 'Municipio'
      this.updatePerPage();
    }
  },

  methods: {
    async cargarEstadisticas() {
      try {
          const response = await apiService.get(import.meta.env.VITE_API_URL + "actividades/estadisticas" , {
              params: {
                  tipo_taller: this.tipoTaller,
                  param_agrupacion: this.paramAgrupacion,
                  tipo_actividad: this.tipoActividad,
                  page: this.page,
                  per_page: this.perPage,
              },
          });
          this.estadisticas = response.data.estadisticas;
          this.cantPages = response.data.total;
      } catch (error) {
          this.errores.push(error);
      }
    },

    async cargarActividades() {
      const actividad = this.tipoTaller == 'Espacio Grupal en el Dispositivo' ? 'actividades_internas' : 'actividades_externas'
    
      await apiService.get(import.meta.env.VITE_API_URL + "actividades/" + actividad)
        .then((response) => {
            this.actividades = response.data;
        })
        .catch((e) => {
            console.log(e)
            this.errores.push(e);
        })
    },

    previousPage() {
      if (this.page > 1) {
        this.page--;
        this.cargarEstadisticas();
      }
    },
    nextPage() {
      if (this.page < this.cantPages){
        this.page++;
        this.cargarEstadisticas();
      }
    },
    updatePerPage() {
      this.page = 1;
      this.cargarEstadisticas();
    },
  },

}
</script>