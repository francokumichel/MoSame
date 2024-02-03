<template>
    <div class="table-responsive table-content border border-secondary-subtle shadow">
        <div class="bg-light d-flex justify-content-center align-items-center g-3 p-4">
            <input class="form-control w-75 me-3 border border-dark-subtle" v-model="searchQuery" type="text" placeholder="Ingrese algún teléfono, nombre, apellido, DNI o municipio" />            
            <button @click="updatePerPage" type="button" class="btn btn-outline-success rounded-circle">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                </svg>
            </button>
        </div>
        <Llamadas0800List :llamadas="llamadas" />
        <div class="d-flex flex-row justify-content-center align-items-center">
            <router-link :to="'/modulo_0800/cargar_llamada'" class="ms-4 mb-3 btn btn-outline-success shadow-sm">Cargar llamada</router-link>
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
import Llamadas0800List from "./Llamadas0800List.vue";

export default {
    data() {
        return {
            llamadas: [],
            searchQuery: "",
            errors: [],
            page: 1,
            perPage: 1,
            cantPages: 0,
        };
    },

    async created() {
        this.loadLlamadas0800();
    },

    components: { Llamadas0800List },

    computed: {
        pageInfo() {
            const start = (this.page - 1) * this.perPage + 1;
            const end = Math.min(start + this.perPage - 1, this.cantPages);
            return `${start}-${end} de ${this.cantPages}`;
        }
    },

    methods: {
        async loadLlamadas0800() {
            try {
                const response = await apiService.get(import.meta.env.VITE_API_URL + "0800/llamadas" , {
                    params: {
                        q: this.searchQuery,
                        page: this.page,
                        per_page: this.perPage,
                    },
                });
                this.llamadas = response.data.llamadas;
                this.cantPages = response.data.total;
            } catch (error) {
                this.errors.push(error);
            }
        },

        previousPage() {
            if (this.page > 1) {
                this.page--;
                this.loadLlamadas0800();
            }
        },
        nextPage() {
            if (this.page < this.cantPages){
                this.page++;
                this.loadLlamadas0800();
            }
        },
        updatePerPage() {
            this.page = 1;
            this.loadLlamadas0800();
        },
    },    
};

</script>