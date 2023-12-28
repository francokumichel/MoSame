<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Usuarios</h1>
    </div>
    <div class="container">
        <FormUsers />
    </div>
</template>

<script>
import FormUsers from "@/components/FormUsers.vue";

export default {
    name: "FormUserView",
    components: {
        FormUsers,
    }
};
</script>