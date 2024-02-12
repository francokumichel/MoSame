<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">0800</h1>
    </div>
    <div class="container w-75 mb-5">
        <FormularioEditarOpciones />
    </div>
</template>

<script>
import FormularioEditarOpciones from "@/components/modulo-general/FormularioEditarOpciones.vue"

export default {
    name: "EditarOpcionesView",
    components: {
        FormularioEditarOpciones,
    }
};
</script>

<style>

</style>