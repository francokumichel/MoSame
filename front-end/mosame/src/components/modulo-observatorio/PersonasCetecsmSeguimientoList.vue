<template>
    <table v-if="personas" class="table table-sm table-hover">
        <thead class="table-light">
            <tr>
                <th scope="col">Región sanitaria</th>                
                <th scope="col">Edad</th>
                <th scope="col">Identidad de género</th>
                <th scope="col">Motivo del acompañamiento</th>
                <th scope="col">Tipo de malestar emocional</th>
                <th scope="col">Resolución del último llamado</th>
                <th scope="col">Fecha de la primera llamada</th>
                <th scope="col">Resolución de la primera llamada</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="persona in personas" :key="persona">
                <td>{{ persona.region_sanitaria }}</td>
                <td>{{ persona.edad }}</td>
                <td>{{ persona.identidad_genero }}</td>
                <td>{{ persona.motivo_acompanamiento }}</td>
                <td>{{ persona.tipo_malestar_emocional ? persona.tipo_malestar_emocional : "-" }}</td>
                <td>{{ persona.resolucion_ultima_llamada }}</td>
                <td>{{ persona.fecha_primera_llamada }}</td>
                <td>{{ persona.resolucion_primera_llamada }}</td>
            </tr>
        </tbody>
    </table>
    <p v-else>No hay personas asignadas registradas en el sistema</p>    
</template>
  
<script>
export default {
    name: "PersonasCetecsmAsignadasList",
    props: {
        personas: {
            type: Array,
            default: () => [],
        },
    },
};
</script>