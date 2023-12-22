<template>
    <UsersList :users="users" />
    <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
            <li @click="previousPage" :class="{ 'disabled': page === 1 }" class="page-item">
            <a class="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
            </a>
            </li>
            <li class="page-item"><a class="page-link" href="#">{{ page }}</a></li>
            <li @click="nextPage" :class="{ 'disabled': page >= this.cantPages }" class="page-item">
            <a class="page-link" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
            </a>
            </li>
        </ul>
    </nav>
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
            perPage: 1,
            cantPages: 0,
        };
    },

    async created() {
        this.loadUsers();
    },

    components: { UsersList },

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

    },
}
</script>