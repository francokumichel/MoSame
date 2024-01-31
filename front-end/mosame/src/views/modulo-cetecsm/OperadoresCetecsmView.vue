<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas</h1>
    </div>
    <div class="container">
        <OperadoresCetecsm />
    </div>
</template>

<script>
    import OperadoresCetecsm from "@/components/modulo-cetecsm/coordinador-cetecsm/OperadoresCetecsm.vue";

    export default {
        name: "OperadoresCetecsmView",
        components: {
            OperadoresCetecsm,
        },
    };
</script>