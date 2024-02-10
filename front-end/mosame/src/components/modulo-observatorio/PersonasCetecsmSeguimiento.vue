<template>
    <div class="offcanvas offcanvas-start" data-bs-scroll="true" tabindex="-1" id="offcanvasWithBothOptions" aria-labelledby="offcanvasWithBothOptionsLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasWithBothOptionsLabel">Filtros</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <fieldset class="row mb-3">
                <legend class="col-form-label col-auto pt-0 fw-semibold">Regiones sanitarias:</legend>
                <div v-for="region_sanitaria in regiones_sanitarias" :key="region_sanitaria" :value="region_sanitaria.tipo" class="form-check">
                    <input
                        class="form-check-input shadow-sm"
                        type="checkbox"
                        :id="region_sanitaria.tipo"
                        :value="region_sanitaria.tipo"
                        @change="actualizarLista(regiones_seleccionadas, region_sanitaria)"
                    />
                    <label :for="region_sanitaria" class="form-check-label">{{ region_sanitaria.tipo }}</label>
                </div>    
            </fieldset>
            <div class="mb-3">
                <label for="fecha_derivacion" class="col-form-label fw-semibold">Fecha de primera llamada:</label>
                <div class="row g-3">
                    <div class="col-auto">
                        <label for="fecha_desde" class="col-form-label">Desde:</label>
                        <input v-model="fecha_desde" type="date" class="form-control shadow-sm" placeholder="Desde" aria-label="fecha_desde">
                    </div>
                    <div class="col-auto">
                        <label for="fecha_hasta" class="col-form-label">Hasta:</label>
                        <input v-model="fecha_hasta" type="date" class="form-control shadow-sm" placeholder="Hasta" aria-label="fecha_hasta">
                    </div>
                </div>
            </div>
            <div class="mb-3">
                <label for="edad" class="col-form-label fw-semibold">Edad:</label>
                <div class="row g-3">
                    <div class="col-3">
                        <label for="edad_desde" class="col-form-label">Desde:</label>
                        <input v-model="edad_desde" type="number" min="0" max="100" class="form-control shadow-sm" placeholder="Desde" aria-label="fecha_desde">
                    </div>
                    <div class="col-3">
                        <label for="edad_hasta" class="col-form-label">Hasta:</label>
                        <input v-model="edad_hasta" type="number" min="0" max="100" class="form-control shadow-sm" placeholder="Hasta" aria-label="fecha_hasta">
                    </div>
                </div>
            </div>
            <div class="mb-3">
                <label for="identidad_genero" class="col-form-label fw-semibold">Identidad de género:</label>
                <select class="form-select border border-dark-subtle" v-model="identidad_genero" aria-label="Default select example">
                    <option></option>
                    <option v-for="identidad in identidades_genero" :key="identidad" :value="identidad.tipo">
                        {{ identidad.tipo }}
                    </option>
                </select>
            </div>
            <div class="mb-3">
                <label for="mot_gral_derivacion" class="col-form-label fw-semibold">Motivo general de acompañamiento:</label>
                <select class="form-select border border-dark-subtle" v-model="mot_gral_acomp" aria-label="Default select example">
                    <option></option>
                    <option v-for="motivo in motivos_grales_acomp" :key="motivo" :value="motivo.tipo">
                        {{ motivo.tipo }}
                    </option>
                </select>
            </div>
            <button @click="updatePerPage" type="button" class="btn btn-primary shadow">Buscar</button>
        </div>
    </div>
    <div class="table-responsive table-content border border-secondary-subtle shadow">
        <PersonasCetecsmSeguimientoList :personas="personas" />
        <div class="d-flex flex-row justify-content-center align-items-center">
            <div class="d-flex flex-row align-items-center">
                <button class="ms-4 mb-3 btn btn-outline-success shadow-sm" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasWithBothOptions" aria-controls="offcanvasWithBothOptions">Agregar filtros</button>
                <button @click="exportarDatos()" class="ms-4 mb-3 btn btn-outline-primary shadow-sm" type="button">Exportar</button>
            </div>
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
import { saveAs } from 'file-saver';
import { apiService } from "@/services/api";
import { displayError, displaySuccess } from "@/services/handlers.js"
import PersonasCetecsmSeguimientoList from "./PersonasCetecsmSeguimientoList.vue";

export default {
    data() {
        return {
            personas: [],
            regiones_seleccionadas: [],
            regiones_sanitarias: [],
            fecha_desde: null,
            fecha_hasta: null,
            edad_desde: null,
            edad_hasta: null,
            identidad_genero: '',
            identidades_genero: [],
            mot_gral_acomp: "",
            motivos_grales_acomp: [],
            errors: [],
            page: 1,
            perPage: 5,
            cantPages: 0,
        };
    },

    async created() {
        this.cargarPersonasEnSeguimiento();
        await apiService.get(import.meta.env.VITE_API_URL + "regiones_sanitarias")
            .then((response) => {
                this.regiones_sanitarias = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            });
        
        await apiService.get(import.meta.env.VITE_API_URL + "mot_grales_acomp")
            .then((response) => {
                this.motivos_grales_acomp = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
        
        await apiService.get(import.meta.env.VITE_API_URL + "identidades_genero")
            .then((response) => {
                this.identidades_genero = response.data;
            })
            .catch((e) => {
                console.log(e)
                this.errores.push(e);
            })
    },

    components: { PersonasCetecsmSeguimientoList },

    computed: {
        pageInfo() {
            const start = (this.page - 1) * this.perPage + 1;
            const end = Math.min(start + this.perPage - 1, this.cantPages);
            return `${start}-${end} de ${this.cantPages}`;
        },

        regionesSeleccionadasString() {
            return this.regiones_seleccionadas.join(',');
        },
    },

    methods: {
        async cargarPersonasEnSeguimiento() {
            try {
                const response = await apiService.get(import.meta.env.VITE_API_URL + "observatorio/personas_cetecsm_seguimiento" , {
                    params: {
                        regiones_seleccionadas: this.regionesSeleccionadasString,
                        fecha_desde: this.fecha_desde,
                        fecha_hasta: this.fecha_hasta,
                        edad_desde: this.edad_desde,
                        edad_hasta: this.edad_hasta,
                        identidad_genero: this.identidad_genero,
                        mot_gral_acomp: this.mot_gral_acomp,
                        page: this.page,
                        per_page: this.perPage,
                    },
                });
                this.personas = response.data.personas;
                this.cantPages = response.data.total;
            } catch (error) {
                this.errors.push(error);
            }
        },

        previousPage() {
            if (this.page > 1) {
                this.page--;
                this.cargarPersonasEnSeguimiento();
            }
        },
        nextPage() {
            if (this.page < this.cantPages){
                this.page++;
                this.cargarPersonasEnSeguimiento();
            }
        },
        updatePerPage() {
            this.page = 1;
            this.cargarPersonasEnSeguimiento();
        },

        actualizarLista(lista, elemento) {
            if (this.chequearLista(lista, elemento)) {
                lista.splice(lista.indexOf(elemento), 1); 
            } else {
                lista.push(elemento.tipo)
            }
        },

        chequearLista(lista, elemento) {
            return lista.some((l) => l == elemento.tipo)
        },

        async exportarDatos() {
            await apiService.get(import.meta.env.VITE_API_URL + "observatorio/personas_cetecsm_seguimiento/exportar" , {
                    params: {
                        regiones_seleccionadas: this.regionesSeleccionadasString,
                        fecha_desde: this.fecha_desde,
                        fecha_hasta: this.fecha_hasta,
                        edad_desde: this.edad_desde,
                        edad_hasta: this.edad_hasta,
                        identidad_genero: this.identidad_genero,
                        mot_gral_derivacion: this.mot_gral_derivacion,
                    },})
                .then((response) => {
                    if(response.status == 200) {
                        const blob = new Blob([response.data], { type: 'text/csv;charset=utf-8' });
                        saveAs(blob, 'personas_en_seguimiento.csv');
                        displaySuccess(this.$toast, "Archivo exportado exitosamente.")
                    }
                })
                .catch((e) => {
                    displayError(this.$toast, e)
                    this.errores.push(e);
                });
        }
    },    
};

</script>