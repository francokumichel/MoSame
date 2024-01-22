<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas</h1>
    </div>
    <div class="container">
        <PersonasAsignadasTodasCetecsm />
    </div>
</template>

<script>
    import PersonasAsignadasTodasCetecsm from "@/components/modulo-cetecsm/coordinador-cetecsm/PersonasAsignadasTodasCetecsm.vue";

    export default {
        name: "PersonasAsignadasTodasCetecsmView",
        components: {
            PersonasAsignadasTodasCetecsm,
        },
    };
</script>