<template>
    <table v-if="llamadas" class="table table-hover">
        <thead class="table-light">
            <tr>
                <th scope="col">Fecha de llamado</th>
                <th scope="col">Detalle</th>
                <th scope="col">Resolución</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="llamada in llamadas" :key="llamada">
                <td>{{ llamada.fecha_llamado }}</td>
                <td>{{ llamada.detalle }}</td>
                <td>{{ llamada.resolucion }}</td>
            </tr>
        </tbody>
    </table>
    <p v-else>No hay usuarios registrados en el sistema</p>    
</template>

<script>
export default {
    name: "PersonaCetecsmLlamadasList",
    props: {
        llamadas: {
            type: Array,
            default: () => [],
        },
    },
};
</script>