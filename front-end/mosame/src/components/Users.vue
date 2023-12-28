<template>
    <div class="table-responsive table-content border border-secondary-subtle shadow">
        <UsersList :users="users" />
        <div class="d-flex flex-row justify-content-center align-items-center">
            <router-link :to="'/users/create'" class="ms-4 mb-3 btn btn-outline-success shadow-sm">Registrar usuario</router-link>
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
import UsersList from "./UsersList.vue";
import { apiService } from "@/services/api";

export default {
    data() {
        return {
            users: [],
            errors: [],
            page: 1,
            perPage: 2,
            cantPages: 0,
        };
    },

    async created() {
        this.loadUsers();
    },

    components: { UsersList },

    computed: {
        pageInfo() {
            const start = (this.page - 1) * this.perPage + 1;
            const end = Math.min(start + this.perPage - 1, this.cantPages);
            return `${start}-${end} de ${this.cantPages}`;
        }
    },

    methods: {
        async loadUsers() {
            try {
                const response = await apiService.get(import.meta.env.VITE_API_URL + "users/index" , {
                    params: {
                        page: this.page,
                        per_page: this.perPage,
                    },
                });
                this.users = response.data.users;
                this.cantPages = response.data.total;
            } catch (error) {
                this.errors.push(error);
            }
        },

        previousPage() {
            if (this.page > 1) {
                this.page--;
                this.loadUsers();
            }
        },
        nextPage() {
            if (this.page < this.cantPages){
                this.page++;
                this.loadUsers();
            }
        },
        updatePerPage() {
            this.page = 1;
            this.loadUsers();
        },

    },
}
</script>

<style>

</style>