<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">Talleres</h1>
    </div>
    <div class="container">
        <TallerForm />
    </div>
</template>

<script>
    import TallerForm from "@/components/modulo-actividades-prevencion/TallerForm.vue";

    export default {
        name: "TallerFormView",
        components: {
            TallerForm,
        },
    };
</script>