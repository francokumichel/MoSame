<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas</h1>
    </div>
    <div class="container">
        <PersonasCetecsm />
    </div>
</template>

<script>
    import PersonasCetecsm from "@/components/modulo-cetecsm/personas-cetecsm/PersonasCetecsm.vue";

    export default {
        name: "PersonaCetecsmView",
        components: {
            PersonasCetecsm,
        },
    };
</script>