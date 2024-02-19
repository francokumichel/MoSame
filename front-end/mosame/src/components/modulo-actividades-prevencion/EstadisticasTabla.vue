<template>
    <table v-if="estadisticas.length > 0" class="table table-sm table-hover">
        <thead class="table-light">
            <tr>
                <th scope="col">{{ paramAgrupacion }}</th>
                <th scope="col">Cantidad talleres</th>
                <th v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" scope="col">Cantidad encuentros</th>
                <th v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" scope="col">Cantidad escuelas</th>
                <th scope="col">{{ tipoTaller == 'Talleres de Salud Mental en las Escuelas' ? 'Cantidad estudiantes' : 'Cantidad participantes' }}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="estadistica in estadisticas" :key="estadistica">
                <td>{{ estadistica.agrupado_por }}</td>
                <td>{{ estadistica.cantidad_talleres }}</td>
                <td v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" >{{ estadistica.cantidad_encuentros }}</td>
                <td v-if="tipoTaller == 'Talleres de Salud Mental en las Escuelas'" >{{ estadistica.cantidad_escuelas }}</td>
                <td>{{ estadistica.cantidad_participantes }}</td>
            </tr>
        </tbody>
    </table>
    <p v-else class="text-center fw-semibold">No hay talleres registrados que cumplan con los párametros ingresados</p>
</template>

<script>
export default {
    name: "TallerList",
    props: {
        estadisticas: {
            type: Array,
            default: () => [],
        },
        tipoTaller: {
            type: String,
            default: () => '',
        },
        paramAgrupacion: {
            type: String,
            default: () => '',
        },
    },
}    
</script>