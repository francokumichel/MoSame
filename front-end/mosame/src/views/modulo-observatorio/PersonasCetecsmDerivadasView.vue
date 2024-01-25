<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas derivadas</h1>
    </div>
    <div class="container">
        <PersonasCetecsmDerivadas />
    </div>
</template>

<script>
    import PersonasCetecsmDerivadas from "@/components/modulo-observatorio/PersonasCetecsmDerivadas.vue";

    export default {
        name: "PersonasCetecsmDerivadasView",
        components: {
            PersonasCetecsmDerivadas,
        },
    };
</script>