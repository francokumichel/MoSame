<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas en seguimiento</h1>
    </div>
    <div class="container">
        <PersonasCetecsmSeguimiento />
    </div>
</template>

<script>
    import PersonasCetecsmSeguimiento from "@/components/modulo-observatorio/PersonasCetecsmSeguimiento.vue";

    export default {
        name: "PersonasCetecsmSeguimientoView",
        components: {
            PersonasCetecsmSeguimiento,
        },
    };
</script>