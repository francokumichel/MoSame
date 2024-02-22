<template>
    <div class="table-responsive table-content border border-secondary-subtle shadow">
        <div class="bg-light d-flex justify-content-center align-items-center g-3 p-4">
            <input class="form-control w-75 me-3 border border-dark-subtle" v-model="searchQuery" type="text" placeholder="Ingrese nombre o apellido" />            
            <button @click="updatePerPage" type="button" class="btn btn-outline-success rounded-circle">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                </svg>
            </button>
        </div>
        <PersonasCetecsmAsignadasList :personasAsignadas="personasAsignadas" :esCoordinador="esCoordinador" />
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
import { apiService } from "@/services/api";
import PersonasCetecsmAsignadasList from "./PersonasCetecsmAsignadasList.vue";

export default {
    data() {
        return {
            personasAsignadas: [],
            searchQuery: "",
            errors: [],
            page: 1,
            perPage: 5,
            cantPages: 0,
            esCoordinador: false,
        };
    },

    async created() {
        this.esCoordinador = this.$route.params.id ? true : false;
        this.cargarAsignadas();
    },

    components: { PersonasCetecsmAsignadasList },

    computed: {
        pageInfo() {
            const start = (this.page - 1) * this.perPage + 1;
            const end = Math.min(start + this.perPage - 1, this.cantPages);
            return `${start}-${end} de ${this.cantPages}`;
        }
    },

    methods: {
        async cargarAsignadas() {
            const endpoint = !this.esCoordinador ? "me/personas_asignadas" : "cetecsm/personasAsignadas/" + this.$route.params.id;
            try {
                const response = await apiService.get(import.meta.env.VITE_API_URL + endpoint , {
                    params: {
                        q: this.searchQuery,
                        page: this.page,
                        per_page: this.perPage,
                    },
                });
                this.personasAsignadas = response.data.personas;
                this.cantPages = response.data.total;
                this.personasAsignadas = this.ordenarPersonasPorFecha()
            } catch (error) {
                this.errors.push(error);
            }
        },

        previousPage() {
            if (this.page > 1) {
                this.page--;
                this.cargarAsignadas();
            }
        },
        nextPage() {
            if (this.page < this.cantPages){
                this.page++;
                this.cargarAsignadas();
            }
        },
        updatePerPage() {
            this.page = 1;
            this.cargarAsignadas();
        },

        ordenarPersonasPorFecha() {
            return this.personasAsignadas.sort((a, b) => {
                if (!a.fecha_prox_llamado_actual && !b.fecha_prox_llamado_actual) {
                    return 0;
                }
                if (!a.fecha_prox_llamado_actual) {
                    return 1;
                }
                if (!b.fecha_prox_llamado_actual) {
                    return -1;
                }

                return new Date(a.fecha_prox_llamado_actual) - new Date(b.fecha_prox_llamado_actual);
            });
        },
    },    
};

</script>