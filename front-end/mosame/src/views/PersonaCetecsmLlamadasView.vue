<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas</h1>
    </div>
    <div class="container">
        <PersonaCetecsmLlamadas />
    </div>
</template>

<script>
    import PersonaCetecsmLlamadas from "@/components/modulo-cetecsm/personas-cetecsm/PersonaCetecsmLlamadas.vue";

    export default {
        name: "PersonaCetecsmLlamadasView",
        components: {
            PersonaCetecsmLlamadas,
        },
    };
</script>