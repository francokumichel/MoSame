<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Llamadas</h1>
    </div>
    <div class="container border border-secondary-subtle shadow">
        <CantidadLlamadasCetecsm />
    </div>
</template>

<script>
    import CantidadLlamadasCetecsm from "@/components/modulo-observatorio/CantidadLlamadasCetecsm.vue";

    export default {
        name: "CantidadLlamadasCetecsmView",
        components: {
            CantidadLlamadasCetecsm,
        },
    };
</script>