<template>
    <div class="table-responsive table-content table-sm border border-secondary-subtle shadow">
        <div class="d-flex flex-row align-items-center m-3">
            <label for="tipos_actividad col-auto">Tipo taller: </label>
            <div class="col-auto ms-3">
                <select class="form-select" v-model="tipoTaller" @change="updatePerPage" aria-label="Default select example">
                    <option v-for="tipo in tiposTaller" :key="tipo" :value="tipo">{{ tipo }}</option>
                </select>
            </div>
        </div>
        <TallerList :talleres="talleres" :tipoTaller="tipoTaller" />
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
import TallerList from "./TallerList.vue";

export default {
    data() {
        return {
            talleres: [],
            tiposTaller: [],
            tipoTaller: '',
            errores: [],
            page: 1,
            perPage: 1,
            cantPages: 0,
        };
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
        
        this.cargarTalleres();
    },

    components: { TallerList },

    computed: {
        pageInfo() {
            const start = (this.page - 1) * this.perPage + 1;
            const end = Math.min(start + this.perPage - 1, this.cantPages);
            return `${start}-${end} de ${this.cantPages}`;
        }
    },

    methods: {
        async cargarTalleres() {
            try {
                const response = await apiService.get(import.meta.env.VITE_API_URL + "actividades/talleres" , {
                    params: {
                        tipo_taller: this.tipoTaller,
                        page: this.page,
                        per_page: this.perPage,
                    },
                });
                this.talleres = response.data.talleres;
                this.cantPages = response.data.total;
            } catch (error) {
                console.log(error)
                this.errores.push(error);
            }
        },

        previousPage() {
            if (this.page > 1) {
                this.page--;
                this.cargarTalleres();
            }
        },
        nextPage() {
            if (this.page < this.cantPages){
                this.page++;
                this.cargarTalleres();
            }
        },
        updatePerPage() {
            this.page = 1;
            this.cargarTalleres();
        },
    },    
};

</script>