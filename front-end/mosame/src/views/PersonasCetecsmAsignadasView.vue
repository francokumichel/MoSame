<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas</h1>
    </div>
    <div class="container">
        <PersonasCetecsmAsignadas />
    </div>
</template>

<script>
    import PersonasCetecsmAsignadas from "@/components/modulo-cetecsm/personas-cetecsm/PersonasCetecsmAsignadas.vue";

    export default {
        name: "PersonaCetecsmAsignadasView",
        components: {
            PersonasCetecsmAsignadas,
        },
    };
</script>