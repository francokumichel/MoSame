<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Estadísticas</h1>
    </div>
    <div class="container">
        <EstadisticasParciales />
    </div>
</template>

<script>
    import EstadisticasParciales from "@/components/modulo-actividades-prevencion/EstadisticasParciales.vue";

    export default {
        name: "EstadisticasView",
        components: {
            EstadisticasParciales,
        },
    };
</script>