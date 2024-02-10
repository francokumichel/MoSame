<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">0800</h1>
    </div>
    <div class="container w-75 mb-5">
        <FormularioCreateLlamada0800 />
    </div>
</template>

<script>
import FormularioCreateLlamada0800 from "@/components/modulo-0800/FormularioCreateLlamada0800.vue"

export default {
    name: "CreateLlamada0800View",
    components: {
        FormularioCreateLlamada0800,
    }
};
</script>

<style>

</style>