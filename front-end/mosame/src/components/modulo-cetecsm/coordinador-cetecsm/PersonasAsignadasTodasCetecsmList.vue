<template>
<table v-if="personasCetecsm" class="table table-hover">
    <thead class="table-light">
        <tr>
            <th scope="col">Nombre</th>
            <th scope="col">Apellido</th>
            <th scope="col">Cantidad de veces llamado</th>
            <th scope="col">Email operador a cargo</th>
            <th scope="col">Resolución del último llamado</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="persona in personasCetecsm" :key="persona">
            <td>{{ persona.nombre }}</td>
            <td>{{ persona.apellido }}</td>
            <td>{{ persona.cantidad_llamadas }}</td>
            <td>{{ persona.email_operador }}</td>
            <td>{{ persona.resolucion_ultima_llamada }}</td>
        </tr>
    </tbody>
</table>
<p v-else>No hay personas en seguimiento registradas.</p>    
</template>
  
<script>
export default {
    name: "PersonasAsignadasTodasCetecsmList",
    props: {
        personasCetecsm: {
            type: Array,
            default: () => [],
        },
    },
};
</script>