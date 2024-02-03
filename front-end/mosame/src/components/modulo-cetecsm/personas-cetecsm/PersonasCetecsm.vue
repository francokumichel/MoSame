<template>
    <div class="table-responsive table-content border border-secondary-subtle shadow">
        <PersonasCetecsmList :personasCetecsm="personasCetecsm" @asignacionRealizada="loadPersonaCetecsm" />
        <div class="d-flex flex-row justify-content-center align-items-center">
            <router-link v-if="this.$store.state.rolActual == 'Operador CETECSM'" :to="'/cetecsm/derivacion/create'" class="ms-4 mb-3 btn btn-outline-success shadow-sm">Registrar derivacion</router-link>
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
import PersonasCetecsmList from "./PersonasCetecsmList.vue";

export default {
    data() {
        return {
            personasCetecsm: [],
            searchQuery: "",
            errors: [],
            page: 1,
            perPage: 5,
            cantPages: 0,
        };
    },

    async created() {
        this.loadPersonaCetecsm();
    },

    components: { PersonasCetecsmList },

    computed: {
        pageInfo() {
            const start = (this.page - 1) * this.perPage + 1;
            const end = Math.min(start + this.perPage - 1, this.cantPages);
            return `${start}-${end} de ${this.cantPages}`;
        }
    },

    methods: {
        async loadPersonaCetecsm() {
            try {
                const response = await apiService.get(import.meta.env.VITE_API_URL + "cetecsm/personas" , {
                    params: {
                        q: this.searchQuery,
                        page: this.page,
                        per_page: this.perPage,
                    },
                });
                this.personasCetecsm = response.data.personas;
                this.cantPages = response.data.total;
            } catch (error) {
                this.errors.push(error);
            }
        },

        previousPage() {
            if (this.page > 1) {
                this.page--;
                this.loadPersonaCetecsm();
            }
        },
        nextPage() {
            if (this.page < this.cantPages){
                this.page++;
                this.loadPersonaCetecsm();
            }
        },
        updatePerPage() {
            this.page = 1;
            this.loadPersonaCetecsm();
        },
    },    
};

</script>