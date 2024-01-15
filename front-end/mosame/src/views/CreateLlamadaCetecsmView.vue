<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Llamadas</h1>
    </div>
    <div class="container">
        <CreateLlamadaCetecsm />
    </div>
</template>

<script>
    import CreateLlamadaCetecsm from "@/components/modulo-cetecsm/llamadas-cetecsm/CreateLlamadaCetecsm.vue";

    export default {
        name: "CreateLlamadaCetecsmView",
        components: {
            CreateLlamadaCetecsm,
        },
    };
</script>