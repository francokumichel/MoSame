<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Talleres</h1>
    </div>
    <div class="container">
        <ObservatorioTalleres />
    </div>
</template>

<script>
    import ObservatorioTalleres from "@/components/modulo-observatorio/ObservatorioTalleres.vue";

    export default {
        name: "ObservatorioTalleresView",
        components: {
    ObservatorioTalleres,
},
    };
</script>