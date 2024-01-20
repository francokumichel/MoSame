<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Personas</h1>
    </div>
    <div class="container">
        <EditarPersonaCetecsmAsignada />
    </div>
</template>

<script>
    import EditarPersonaCetecsmAsignada from "@/components/modulo-cetecsm/personas-cetecsm/EditarPersonaCetecsmAsignada.vue";

    export default {
        name: "EditarPersonaCetecsmAsignadaView",
        components: {
            EditarPersonaCetecsmAsignada,
        },
    };
</script>