<template>
    <div class="pt-2 mb-4 border-2 border-bottom border-info">
        <h1 class="title text-info fw-bold ms-5">0800</h1>
    </div>
    <div class="container">
        <Llamadas0800/>
    </div>
</template>

<script>
    import Llamadas0800 from "@/components/modulo-0800/Llamadas0800.vue";

    export default {
        name: "Llamadas0800View",
        components: {
            Llamadas0800,
        },
    };
</script>