<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Talleres</h1>
    </div>
    <div class="container">
        <Taller />
    </div>
</template>

<script>
    import Taller from "@/components/modulo-actividades-prevencion/Taller.vue";

    export default {
        name: "TallerView",
        components: {
            Taller,
        },
    };
</script>