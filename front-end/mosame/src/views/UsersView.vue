<template>
    <div class="bg-light py-2">
        <h2 class="title ms-2">Usuarios</h2>
    </div>
    <div class="container">
        <Users />
    </div>
</template>

<script>
    import Users from "@/components/Users.vue";

    export default {
        name: "UsersView",
        components: {
            Users,
        },
    };
</script>