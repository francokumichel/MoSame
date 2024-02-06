<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Llamadas 0800</h1>
    </div>
    <div class="container">
        <ObservatorioLlamadas0800 />
    </div>
</template>

<script>
    import ObservatorioLlamadas0800 from "@/components/modulo-observatorio/ObservatorioLlamadas0800.vue";

    export default {
        name: "ObservatorioLlamadas0800View",
        components: {
            ObservatorioLlamadas0800,
        },
    };
</script>