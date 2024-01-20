<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas</h1>
    </div>
    <div class="container">
        <PerfilPersonaCetecsm />
    </div>
</template>

<script>
    import PerfilPersonaCetecsm from "@/components/modulo-cetecsm/personas-cetecsm/PerfilPersonaCetecsm.vue";

    export default {
        name: "PefilPersonaCetecsmView",
        components: {
            PerfilPersonaCetecsm,
        },
    };
</script>