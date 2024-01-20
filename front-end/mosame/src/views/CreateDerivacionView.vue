<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Derivaciones</h1>
    </div>
    <div class="container w-75 mb-5">
        <CreateDerivacion />
    </div>
</template>

<script>
import CreateDerivacion from "@/components/modulo-cetecsm/formularios-derivacion/CreateDerivacion.vue";

export default {
    name: "CreateDerivacionView",
    components: {
        CreateDerivacion,
    }
};
</script>

<style>

</style>